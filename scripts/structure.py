import pandas as pd
from datetime import datetime
from get_data import get_data
from clean_data import clean_data

# get data
path = "../data/Voluntary-Registry-Offsets-Database--v2026-06.xlsx"
df = get_data(path)

# clean data
column_list = [
    "Project ID",
    "Project Name",
    "Voluntary Registry",
    "Scope",
    "Type",
    "Reduction / Removal",
    "Methodology / Protocol",
    "Region",
    "Country",
    "Project Developer",
    "Article 6",
    "CORSIA",
    "ICVCM CCP",
    "Verra CCB"
]

df_vintage, df_issue, df_retirement_cancpytellation = clean_data(df, column_list, 1996, 2026)

# test
#df_vintage.to_csv("vintage.csv") 
#df_issue.to_csv("issue.csv") 
#df_retirement_cancellation.to_csv("retirement_cancellation.csv") 