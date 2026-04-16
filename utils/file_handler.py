import pandas as pd 

def load_csv(file):
    try:
        return pd.read_csv(file)
    except:
        return pd.DataFrame()

def save_csv(df, file):
    df.to_csv(file, index=False)
