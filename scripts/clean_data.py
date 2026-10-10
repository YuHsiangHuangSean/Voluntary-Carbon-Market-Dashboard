import pandas as pd
from get_data import get_data

# clean data
def clean_data(df, column_list, start_year, end_year):

    # convert the datatype of year columns into float
    year_list = range(start_year, end_year+1)
    for year in year_list:
        df[year] = df[year].astype("float64")
        df[str(year + 0.3)] = df[str(year + 0.3)].astype("float64")
        df[str(year + 0.1)] = df[str(year + 0.1)].astype("float64")

    # format object columns
    df["Project Name"] = df["Project Name"].str.title()
    df["Voluntary Registry"] = df["Voluntary Registry"].str.upper()
    df["Scope"] = df["Scope"].str.title()
    df["Type"] = df["Type"].str.title()
    df["Reduction / Removal"] = df["Reduction / Removal"].str.title()
    df["Region"] = df["Region"].str.title()
    df["Country"] = df["Country"].str.title()

    # transform certification column into 4 boolean columns
    certifications = {
        "Article 6": "Article 6 | Article Six",
        "CORSIA": "CORSIA",
        "ICVCM CCP": "ICVCM | CCP",
        "Verra CCB": "CCB"
    }

    for new_col, keyword in certifications.items():
        df[new_col] = df["Certifications"].str.contains(
            keyword,
            case=False,
            na=False
        )

    # create dataframe for issue years
    # Verra may issue credits for the same projects in multiple batches. In the raw data, it is assumed that Verra issues all credits in the first batch
    df_issue = df[column_list + [str(year + 0.3) for year in year_list]]

    columns = {
        str(year + 0.3): year
        for year in year_list
    }

    df_issue = df_issue.rename(columns = columns)

    # create dataframe for retirement or cancellation years
    df_retirement_cancellation = df[column_list + [str(year + 0.1) for year in year_list]]

    columns = {
        str(year + 0.1): year
        for year in year_list
    }

    df_retirement_cancellation = df_retirement_cancellation.rename(columns = columns)

    # export data
    return df_issue, df_retirement_cancellation