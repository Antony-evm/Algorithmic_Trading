import pandas as pd
import numpy as np


def SMA(df: pd.DataFrame, periods: int = 14) -> pd.DataFrame:
    return df.rolling(window=periods).mean()


def EMA(df: pd.DataFrame, periods: int = 14) -> pd.DataFrame:
    return df.ewm(span=periods, min_periods=periods).mean()


def ATR(df: pd.DataFrame, span: int = 14) -> pd.DataFrame:
    high_low = df["High"] - df["Low"]
    high_close = np.abs(df["High"] - df["Close"].shift())
    low_close = np.abs(df["Low"] - df["Close"].shift())
    ranges = pd.concat([high_low, high_close, low_close], axis=1)
    true_range = np.max(ranges, axis=1)
    return true_range.rolling(span).sum() / span
