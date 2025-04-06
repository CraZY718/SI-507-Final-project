import pandas as pd
import numpy as np

def clean_data(df):
    # select useful factors
    required_columns = [
        'TICKER', 'date', 'PRC', 'OPENPRC', 'RET', 'RETX',
        'VOL', 'SHROUT', 'BID', 'ASK', 'BIDLO', 'ASKHI',
        'DIVAMT', 'NUMTRD', 'vwretd', 'sprtrn'
    ]
    df = df[required_columns].copy()

    # convert type
    df['date'] = pd.to_datetime(df['date'])
    numeric_cols = [col for col in required_columns if col != 'TICKER' and col != 'date']
    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors='coerce')

    df.sort_values(by=['TICKER', 'date'], inplace=True)

    # Missing value padding (forward + backward)
    df.fillna(method='ffill', inplace=True)
    df.fillna(method='bfill', inplace=True)
    df.dropna(inplace=True)

    # Add log price (for momentum）
    df['log_prc'] = np.log(df['PRC'].replace(0, np.nan))

    return df.reset_index(drop=True)

