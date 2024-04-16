import pandas as pd

# reads in an excel file and returns a np array
def excel_to_np(file_path):
    df = pd.read_excel(file_path)
    return df.values