import streamlit as st
import pandas as pd
from datetime import datetime
import yfinance as yf


currentDate=datetime.today().strftime('%Y-%m-%d')

currencies = []
dict1={}


options = st.sidebar.multiselect(
     'Enter New Currency',
     ["ZMW","YER","XPF","VND","VED","VES","EUR","VUV","UZS","UYU","USD","GBP","AED","UAH","UGX","AUD","USD","TMT","TRY","TND","TTD","TOP","XOF","THB","TZS","TJS","TWD","SYP","CHF","SEK","SRD","SDG","LKR","SSP","EUR","RUB","ZAR","SOS","SBD","EUR","EUR","ANG","USD","BND","SGD","SLL","SCR","RSD","XOF","SAR","STN","EUR","WST","XCD","XCD","XCD","SHP","MAD","MRU","DZD","USD","RWF","RUB","RON","QAR","EUR","PLN","NZD","PHP","PEN","PYG","PGK","USD","PAB","JOD","ILS","USD","PKR","OMR","NOK","TRY","MKD","NZD","NGN","XOF","NIO","NZD","XPF","EUR","NPR","AUD","ZAR","NAD","MMK","MZN","MAD","XCD","EUR","MNT","EUR","MDL","USD","MXN","MUR","MRU","USD","EUR","XOF","MVR","MYR","MWK","MGA","HKD","MOP","EUR","EUR","CHF","LYD","LRD","ZAR","LSL","LBP","EUR","LAK","KGS","KWD","EUR","KRW","KPW","AUD","KES","KZT","JOD","GBP","JPY","JMD","EUR","ILS","GBP","EUR","IQD","IRR","IDR","INR","ISK","HUF","HKD","HNL","HTG","GYD","XOF","GNF","GBP","GTQ","XCD","DKK","EUR","GIP","GHS","EUR","GEL","GMD","XAF","XPF","EUR","EUR","FJD","DKK","FKP","ETB","ZAR","SZL","EUR","ERN","XAF","USD","EGP","USD","DOP","XCD","DJF","DKK","CZK","EUR","ANG","CUP","HRK","XOF","CRC","NZD","XAF","CDF","KMF","COP","CNY","CLP","XAF","XAF","KYD","CVE","CAD","XAF","KHR","BIF","XOF","BGN","SGD","BND","USD","USD","BRL","BWP","BAM","USD","BOB","INR","BTN","BMD","XOF","BZD","EUR","BYN","BBD","BDT","BHD","BSD","AZN","EUR","AUD","SHP","AWG","AMD","AMD","ARS","XCD","XCD","AOA","EUR","DZD","GBP","EUR","AFN","RUB"],
     ["ZAR","CHF","DKK","INR","SEK","SLL","SOS","SZL","THB","TND","TRY","TTD","TZS","UAH","UGX","UYU","UZS","SGD","VND","XAF","CAD","USD","GBP"])

for i in options:
    currencies.append(i + "USD=X")

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


