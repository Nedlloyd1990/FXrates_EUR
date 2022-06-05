import streamlit as st
import pandas as pd
from datetime import datetime
import yfinance as yf
from datetime import date

st.sidebar.write("Historical Currency Conversion Rate-  EUR")

d = st.sidebar.date_input("Start Date", date(2005, 1, 1))
start_d= d.strftime('%Y-%m-%d')

d1 = st.sidebar.date_input("End Date", datetime.today())
end_d= d.strftime('%Y-%m-%d')

currencies = []
dict1={}


options = st.multiselect(
     'Enter New Currency',
     ["AFN","AOA","AMD","SHP","AZN","BYN","BMD","BTN","USD","BAM","BRL","KYD","CDF","ANG","ERN","FKP","FJD","GEL","GHS","GIP","GYD","IRR","KPW","KGS","LRD","MRU","MNT","MZN","RON","WST","STN","RSD","SBD","SSP","SDG","SRD","SYP","TJS","TOP","TMT","VUV","VES","VED","ZMW","ZAR","YER","XPF","XCD","XAF","VND","SGD","UZS","UYU","UGX","UAH","TZS","TTD","TRY","TND","THB","SZL","SOS","SLL","SEK","SCR","SAR","RWF","RUB","QAR","PYG","PLN","PKR","PHP","PGK","PEN","PAB","OMR","NZD","NPR","NOK","NIO","NGN","NAD","MYR","MXN","MWK","MVR","MUR","MOP","MMK","MKD","MGA","MDL","MAD","LYD","LSL","LKR","LBP","LAK","KZT","KWD","KRW","KMF","KHR","KES","JPY","JOD","JMD","ISK","IQD","INR","ILS","IDR","HUF","HTG","HRK","HNL","HKD","GTQ","GNF","GMD","GBP","EUR","ETB","EGP","DZD","DOP","DKK","DJF","CZK","CVE","CUP","CRC","COP","CNY","CLP","CHF","CAD","BZD","BWP","BSD","BOB","BND","BIF","BHD","BGN","BDT","BBD","AWG","AUD","ARS","ALL","AED","TWD","XOF"],
     ["ZAR","CHF","DKK","INR","SEK","SLL","SOS","SZL","THB","TND","TRY","TTD","TZS","UAH","UGX","UYU","UZS","SGD","VND","XAF","CAD","USD","GBP"])

for i in options:
    currencies.append(i + "EUR=X")

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


