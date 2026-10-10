import pandas as pd

# structure data
def structure_data(df_issue, df_retirement_cancellation, column_list, start_year, end_year):

    unmerged_df_list = []

    # create a project dataframe
    df_project = df_issue[column_list]

    # restructure dataframes by year
    for df in (df_issue, df_retirement_cancellation):

        # drop columns already saved in the project dataframe
        year_list = range(start_year, end_year+1)
        df = df[["Project ID"] + [year for year in year_list]]

        # unpivot year columns
        df = df.melt(
            id_vars = "Project ID",
            var_name = "Year",
            value_name = "Quantity"
        )

        # save restructured dataframe to a list
        unmerged_df_list.append(df)      

    # rename quantity columns
    column_names = ["Issuance", "Retirement/cancellation"]
    for i in range(2):
        unmerged_df_list[i] = unmerged_df_list[i].rename(columns = {"Quantity": column_names[i]})

    # join dataframes
    df_record = pd.merge(unmerged_df_list[0], unmerged_df_list[1], how='outer', on = ["Project ID", "Year"])

    # test
    #print(df_record.info())
    #print("")
    #print(df_record.describe(include="object"))

    # drop rows with zero issuance, retirement/cancellation, and remaining
    df_record = df_record[(df_record["Issuance"] != 0) | (df_record["Retirement/cancellation"] != 0)]

    # format year column
    df_record["Year"] = df_record["Year"].astype("int64")
    
    return df_project, df_record