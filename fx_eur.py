import streamlit as st
import pandas as pd
from datetime import datetime
import yfinance as yf




d = st.date_input("Start Date", date(2019, 7, 6))
start_d= d.strftime('%Y-%m-%d')

d1 = st.date_input("End Date", today())
end_d= d.strftime('%Y-%m-%d')

currencies = []
dict1={}


options = st.sidebar.multiselect(
     'Enter New Currency',
     ["ZMW","YER","VND","VED","VES","VUV","UZS","UYU","AED","UAH","UGX","TMT","TND","TTD","TOP","THB","TZS","TJS","TWD","SYP","SEK","SRD","SDG","LKR","SSP","SOS","SBD","SLL","SCR","RSD","SAR","STN","WST","RWF","RON","QAR","PLN","PHP","PEN","PYG","PGK","PAB","PKR","OMR","NOK","TRY","MKD","NGN","NIO","NPR","NAD","MMK","MZN","MAD","MNT","MDL","MXN","MUR","MRU","MVR","MYR","MWK","MGA","MOP","CHF","LYD","LRD","LSL","LBP","LAK","KGS","KWD","KRW","KPW","KES","KZT","JOD","JPY","JMD","ILS","IQD","IRR","IDR","ISK","HUF","HKD","HNL","HTG","GYD","GNF","GTQ","GIP","GHS","GEL","GMD","XPF","FJD","FKP","ETB","ZAR","SZL","ERN","EGP","DOP","DJF","DKK","CZK","ANG","CUP","HRK","CRC","NZD","CDF","KMF","COP","CNY","CLP","KYD","CVE","CAD","XAF","KHR","BIF","BGN","SGD","BND","BRL","BWP","BAM","USD","BOB","INR","BTN","BMD","XOF","BZD","BYN","BBD","BDT","BHD","BSD","AZN","AUD","SHP","AWG","AMD","ARS","XCD","AOA","DZD","GBP","EUR","AFN","RUB"],
     ["ZAR","CHF","DKK","INR","SEK","SLL","SOS","SZL","THB","TND","TRY","TTD","TZS","UAH","UGX","UYU","UZS","SGD","VND","XAF","CAD","USD","GBP"])

for i in options:
    currencies.append(i + "USD=X")

for ccy in currencies:
	ccy_pair= yf.Ticker(ccy)
	ccy_pair_list = ccy_pair.history(start=str(start_d) ,end=str(d1),  interval="1d")
	dataframe=pd.DataFrame(ccy_pair_list)

	filter2=pd.DataFrame(dataframe).Close
	dict1[ccy]=filter2

d1=pd.DataFrame(dict1, columns=dict1.keys())

@st.cache
def convert_df(df):
   return df.to_csv().encode('utf-8')


csv = convert_df(d1)


st.dataframe(d1)
st.download_button( "Click to Download", csv, "file.csv",  "text/csv",   key='download-csv')


