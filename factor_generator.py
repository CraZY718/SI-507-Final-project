import pandas as pd
import numpy as np

def generate_factors(df, window=10):
    result = pd.DataFrame()
    result['date'] = df['date']

    # Momentum: log(price_t / price_{t-n})
    result['momentum'] = df['log_prc'] - df['log_prc'].shift(window)

    # Volatility: rolling standard deviation of return
    result['volatility'] = df['RET'].rolling(window).std()

    # Liquidity: volume / shares outstanding
    result['liquidity'] = df['VOL'] / df['SHROUT']

    # Amplitude: (high - low) / close price
    result['amplitude'] = (df['ASKHI'] - df['BIDLO']) / df['PRC']

    # Dividend yield: DIVAMT / PRC
    result['dividend_yield'] = df['DIVAMT'] / df['PRC']

    # Gap return: (open - previous close) / previous close
    result['gap_return'] = (df['OPENPRC'] - df['PRC'].shift(1)) / df['PRC'].shift(1)

    # Trading activity: number of trades / rolling mean
    result['trading_activity'] = df['NUMTRD'] / df['NUMTRD'].rolling(window).mean()

    # Market correlation: rolling correlation with market return
    result['market_corr'] = df['RET'].rolling(window).corr(df['vwretd'])

    # Target return as dependent variable
    result['target_return'] = df['RET']

    return result.dropna().reset_index(drop=True)

