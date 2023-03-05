import pandas as pd
import pandas_datareader.data as web
# !pip install yfinance==0.1.62
import yfinance as yf
def save_indexes(interval='1d',sp500=True,ftse100=True):
    yf.pdr_override()

    path = 'Ticker Data//Indexes'
    if sp500:
        print('Downloading SP500')
        df = web.DataReader('^GSPC',interval=interval)
        df.to_parquet(f'{path}//SP500.parquet')
    if ftse100:
        print('Downloading FTSE100')
        df = web.DataReader('^FTSE',interval=interval)
        df.to_parquet(f'{path}//FTSE100.parquet')


def save_tickers(tickers,interval='1d'):
    path = 'Ticker Data//Tickers'
    for ticker in tickers:
        print(f'Downloading {ticker}')
        df = web.DataReader(ticker,interval=interval)
        if len(df)>0:
            df.to_parquet(f'{path}//{ticker}.parquet')

        
    
