import pandas as pd
from datetime import datetime

# Read the excel file as dataframe
def get_data():
    t0 = datetime.now()
    df = pd.read_excel("../data/Voluntary-Registry-Offsets-Database--v2026-06.xlsx", sheet_name = "PROJECTS", header = 3)
    t1 = datetime.now()
    delta = t1 - t0
    print("Reading time: ", delta)
    return df