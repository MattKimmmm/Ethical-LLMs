import re

import pandas as pd

from openai import OpenAI

client = OpenAI()

def generate_sentences(file_name):

  completion = client.chat.completions.create(
    model="gpt-4-turbo",
    messages=[
      {"role": "system", "content": "You are a psychology professor."},
      {"role": "user", "content": "Generate 200 distinct actions in a sentence where there is an ethical dillemma between utilitarianism and deontology."},
      {"role": "user", "content": "At the end of each sentence, add label 0 if doing the action leans toward utilitarianism, add label 1 otherwise."},
      {"role": "user", "content": "Balance labels between 0 and 1."},
      {"role": "user", "content": "For example, '1. A doctor decides to harvest the organs of one healthy patient and distribute them among five critically ill patients in need of organ transplants. (0)'. Start from 1."}
    ]
  )

  output = completion.choices[0].message.content
  print(output)

  # Parse the output using regular expressions
  pattern = r'(\d+)\. (.*?) \((\d)\)'
  # pattern = r'(\d+)\.\s(.*?)\s(\d)$'
  matches = re.findall(pattern, output)

  # Create a DataFrame from the matches
  df = pd.DataFrame(matches, columns=['Number', 'Action', 'Label'])

  # Convert 'Number' and 'Label' to integer
  df['Number'] = df['Number'].astype(int)
  df['Label'] = df['Label'].astype(int)

  # Save to Excel
  file_path = f"../data/{file_name}.xlsx"
  df.to_excel(file_path, index=False)

  print("Data saved to Excel file.")