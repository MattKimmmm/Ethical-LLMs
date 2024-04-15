import re

import pandas as pd

from openai import OpenAI

client = OpenAI()

def generate_sentences(file_name):

  completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
      {"role": "system", "content": "You are a psychology professor."},
      {"role": "user", "content": "Generate 1000 distinct actions in a sentence where there is an ethical dillemma between utilitarianism and deontology."},
      {"role": "user", "content": "At the end of each sentence, add label 0 if doing the action leans toward utilitarianism, add label 1 otherwise."}
    ]
  )

  output = completion.choices[0].message.content
  # print(output)

  # Parse the output using regular expressions
  pattern = r'(\d+)\. (.*?) \((\d)\)'
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