import pandas as pd

def load_data(file):
    return pd.read_csv(file)

def clean_data(df, fill_method="mean"):
    # Handle missing values
    if fill_method == "mean":
        return df.fillna(df.mean())
    elif fill_method == "median":
        return df.fillna(df.median())
    elif fill_method == "drop":
        return df.dropna()
    return df

def select_columns(df, columns):
    return df[columns]
