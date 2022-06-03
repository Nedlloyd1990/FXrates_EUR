import streamlit as st
import pandas as pd
from datetime import datetime
import yfinance as yf


currentDate=datetime.today().strftime('%Y-%m-%d')

currencies = ["GBPEUR=X","USDEUR=X","CADEUR=X"]

dict1={}

for ccy in currencies:
	ccy_pair= yf.Ticker(ccy)
	ccy_pair_list = ccy_pair.history(start="2021-11-14" ,end=str(currentDate),  interval="1d")
	dataframe=pd.DataFrame(ccy_pair_list)

	filter2=pd.DataFrame(dataframe).Close
	dict1[ccy]=filter2

d1=pd.DataFrame(dict1, columns=dict1.keys())

@st.cache
def convert_df(df):
   return df.to_csv().encode('utf-8')


csv = convert_df(d1)


st.dataframe(d1)
#st.download_button(label='Download Current Result',   data=d1 , file_name= 'df_test.xlsx')
st.download_button( "Click to Download", csv, "file.csv",  "text/csv",   key='download-csv')


