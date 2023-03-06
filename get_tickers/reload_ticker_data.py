import pandas as pd
import pandas_datareader.data as web
# !pip install yfinance==0.1.62
import yfinance as yf
def save_indexes(interval:str='1d',sp500:bool=True,ftse100:bool=True)->None:
    '''
    Use hardcoded tickers for indexes to retrieve data in timeseries format from yahoo finance
    Currently available for SP500 & FTSE100
    interval available values 1m, 2m, 5m, 15m, 30m, 60m, 90m, 1h, 1d, 5d, 1wk, 1mo, 3mo
    Period is max as default behavior
    Saves data in the specified paths
    '''
    yf.pdr_override()

    path = 'Ticker Data//Indexes'
    if sp500:
        print('Downloading SP500')
        df = web.DataReader('^GSPC',interval=interval,progress=False,show_errors=False)
        if len(df)==0:
            print('SP500 failed to download')
        else:
            df.to_parquet(f'{path}//SP500.parquet')
    if ftse100:
        print('Downloading FTSE100')
        df = web.DataReader('^FTSE',interval=interval,progress=False,show_errors=False)
        if len(df)==0:
            print('FTSE100 failed to download')
        else:
            df.to_parquet(f'{path}//FTSE100.parquet')


def save_tickers(tickers:list,interval:str='1d',suffix=None)->None:
    '''
    Use given tickers to retrieve data in timeseries format from yahoo finance.
    If ticker is not available it will print an appropriate message to the console
    interval available values 1m, 2m, 5m, 15m, 30m, 60m, 90m, 1h, 1d, 5d, 1wk, 1mo, 3mo
    Period is max as default behavior
    Saves data in the specified paths
    '''
    path = 'Ticker Data//Tickers'
    for idx,ticker in enumerate(tickers):
        print(f'{idx+1}/{len(tickers)}')
        df = web.DataReader(ticker,interval=interval,progress=False,show_errors=False)
        if len(df)==0:
            if suffix:
                df = web.DataReader(ticker+suffix,interval=interval,progress=False,show_errors=False)
        if len(df)==0:
            print(f'{ticker} failed to download')
        else:
            df.to_parquet(f'{path}//{ticker}.parquet')

        
    
