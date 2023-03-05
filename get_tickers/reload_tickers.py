import requests
import pandas as pd

def reload_SP500_tickers():
    url="https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
    df = pd.read_html(url)[0]
    df = df[['Symbol','Security','GICS Sector']]
    df.columns = ['Ticker','Security','Sector']
    return df

def reload_FTSE100_tickers():
    url = 'https://en.wikipedia.org/wiki/FTSE_100_Index'
    df = pd.read_html(url)[4]
    df.columns = ['Security','Ticker','Sector']
    return df[['Ticker','Security','Sector']]
