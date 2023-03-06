import requests
import pandas as pd

def reload_SP500_tickers()->pd.DataFrame:
	'''
	Use wiki URL to retrieve current SP500 tickers
	Returns dataframe that contains the tickers, the name of the companies and the Sector the companies operate in
	If wiki page changes this needs to be revisited
	'''
	url="https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
	df = pd.read_html(url)[0]
	df = df[['Symbol','Security','GICS Sector']]
	df.columns = ['Ticker','Security','Sector']
	df['Ticker'] = df['Ticker'].str.replace('.','-')
	return df

def reload_FTSE100_tickers()->pd.DataFrame:
	'''
	Use wiki URL to retrieve current FTSE100 tickers
	Returns dataframe that contains the tickers, the name of the companies and the Sector the companies operate in
	If wiki page changes this needs to be revisited
	'''
	url = 'https://en.wikipedia.org/wiki/FTSE_100_Index'
	df = pd.read_html(url)[4]
	df.columns = ['Security','Ticker','Sector']
	df['Ticker'] = df['Ticker'].str.replace('.','-')
	return df[['Ticker','Security','Sector']]
