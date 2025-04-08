import pandas as pd

def load_and_clean_data(path):
    df = pd.read_csv(path)
    df.dropna(subset=['text'], inplace=True)
    df['text'] = df['text'].str.strip()
    return df