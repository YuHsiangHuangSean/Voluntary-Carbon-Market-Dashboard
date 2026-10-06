import pandas as pd

# structure data
def structure_data(df, column_list):
    # unpivot year columns
    df = df.melt(
        id_vars = column_list,
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
    
    return df 