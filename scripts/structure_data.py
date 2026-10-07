import pandas as pd

# structure data
def structure_data(df_vintage, df_issue, df_retirement_cancellation, column_list, start_year, end_year):

    output_dfs = []

    # create a project dataframe
    df_project = df_issue[column_list]
    output_dfs.append(df_project)

    # restructure dataframes by year
    for df in (df_vintage, df_issue, df_retirement_cancellation):

        # drop columns already saved in the project dataframe
        year_list = range(start_year, end_year+1)
        df = df[["Project ID"] + [year for year in year_list]]

        # unpivot year columns
        df = df.melt(
            id_vars = "Project ID",
            var_name = "Year",
            value_name = "Quantity"
        )

        # reset index and use it to create a primary key column
        df = df.reset_index(drop=True)
        df["Record ID"] = df.index+1

        # drop rows with zero quantity
        df = df[df["Quantity"] != 0]

        # format year column
        df["Year"] = df["Year"].astype("int64")

        # export dataframes
        output_dfs.append(df)
    
    return output_dfs