import re

import pandas as pd

from openai import OpenAI

client = OpenAI()

def generate_sentences(file_name, persona, num_extra_batches):
  output = generate_sentences_batch_initial(file_name, persona)

  # Parse the output using regular expressions
  pattern = r'(\d+)\. (.*?) \((\d)\)'
  # pattern = r'(\d+)\.\s(.*?)\s(\d)$'
  matches = re.findall(pattern, output)

  for i in range(num_extra_batches):
    output = generate_sentences_batch(file_name, persona, matches)
    matches += re.findall(pattern, output)

  # Create a DataFrame from the matches
  df = pd.DataFrame(matches, columns=['Number', 'Action', 'Label'])

  # Convert 'Number' and 'Label' to integer
  df['Number'] = df['Number'].astype(int)
  df['Label'] = df['Label'].astype(int)

  # Save to Excel
  file_path = f"../data/{file_name}.xlsx"
  df.to_excel(file_path, index=False)

  print("Data saved to Excel file.")


def generate_sentences_batch_initial(file_name, persona):

  completion = client.chat.completions.create(
    model="gpt-4-turbo",
    messages=[
      {"role": "system", "content": persona},
      {"role": "user", "content": "Generate 50 distinct actions in a sentence where there is an ethical dillemma between utilitarianism and deontology."},
      {"role": "user", "content": "At the end of each sentence, add label 0 if doing the action leans toward utilitarianism, add label 1 otherwise."},
      {"role": "user", "content": "Balance labels between 0 and 1."},
      {"role": "user", "content": "For example, '1. A doctor decides to harvest the organs of one healthy patient and distribute them among five critically ill patients in need of organ transplants. (0)'. Start from 1."}
    ],
    # max_tokens=20000
  )

  output = completion.choices[0].message.content
  print(output)

  return output

def generate_sentences_batch(file_name, persona, examples):

  examples_text = " ".join(f"{num}. {action} ({label})" for num, action, label in examples)
  examples_prompt = f"Previously generated examples include: {examples_text}. Do not repeat these."

  completion = client.chat.completions.create(
    model="gpt-4-turbo",
    messages=[
      {"role": "system", "content": persona},
      {"role": "user", "content": examples_prompt},
      {"role": "user", "content": "Generate 50 distinct actions in a sentence where there is an ethical dillemma between utilitarianism and deontology."},
      {"role": "user", "content": "At the end of each sentence, add label 0 if doing the action leans toward utilitarianism, add label 1 otherwise."},
      {"role": "user", "content": "Balance labels between 0 and 1."},
      {"role": "user", "content": "For example, '1. A doctor decides to harvest the organs of one healthy patient and distribute them among five critically ill patients in need of organ transplants. (0)'. Start from 1."}
    ],
    # max_tokens=20000
  )

  output = completion.choices[0].message.content
  print(output)

  return output