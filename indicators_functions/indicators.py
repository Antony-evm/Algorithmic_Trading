import pandas as pd

def SMA(df,periods=14):
	return df.rolling(window=periods).mean()

def EMA(df,periods=14):
	return df.ewm(span=periods,min_periods=periods).mean()

def ATR(df,span=14):
	high_low = df['High'] - df['Low']
    high_close = np.abs(df['High'] - df['Close'].shift())
    low_close = np.abs(df['Low'] - df['Close'].shift())
    ranges = pd.concat([high_low, high_close, low_close], axis=1)
    true_range = np.max(ranges, axis=1)
    return true_range.rolling(span).sum()/span
