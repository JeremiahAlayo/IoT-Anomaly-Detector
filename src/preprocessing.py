import pandas as pd

def clean(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    # Parse common timestamp column names
    for col in ["timestamp", "time", "datetime"]:
        if col in df.columns:
            df[col] = pd.to_datetime(df[col], errors="coerce")
    # Drop fully empty columns
    df = df.dropna(axis=1, how="all")
    return df
