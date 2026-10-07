import pandas as pd
from datetime import datetime

from get_data import get_data
from clean_data import clean_data
from structure_data import structure_data

# record start time
t0 = datetime.now()

# get data
file_name = "Voluntary-Registry-Offsets-Database--v2026-06.xlsx"
path = "data/" + file_name
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
start_year = 1996
end_year = 2026

df_vintage, df_issue, df_retirement_cancellation = clean_data(df, column_list, start_year, end_year)

# structure data
df_project, df_vintage, df_issue, df_retirement_cancellation = structure_data(df_vintage, df_issue, df_retirement_cancellation, column_list, start_year, end_year)

# filter data
q_expression = "Year >= 2016"
df_vintage = df_vintage.query(q_expression)
df_issue = df_issue.query(q_expression)
df_retirement_cancellation = df_retirement_cancellation.query(q_expression)

# export data as csv files
df_project.to_csv("data/project.csv")
df_vintage.to_csv("data/vintage.csv")
df_issue.to_csv("data/issue.csv") 
df_retirement_cancellation.to_csv("data/retirement_cancellation.csv") 

# record end time and display total process time
t1 = datetime.now()
delta = t1 - t0
print("Process time: ", delta)