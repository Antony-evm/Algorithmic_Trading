import pandas as pd

def SMA(periods=14):
	return df.rolling(window=periods).mean()