import pandas as pd

# read the excel file as dataframe
def get_data(path):
    df = pd.read_excel(path, sheet_name = "PROJECTS", header = 3)
    return df