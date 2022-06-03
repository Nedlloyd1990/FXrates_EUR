import streamlit as st
import pandas as pd
from datetime import datetime
import yfinance as yf


currentDate=datetime.today().strftime('%Y-%m-%d')

currencies = ["GBPEUR=X","USDEUR=X","CADEUR=X","XAFEUR=X","VNDEUR=X","SGDEUR=X","UZSEUR=X","UYUEUR=X",
"UGXEUR=X","UAHEUR=X","TZSEUR=X","TTDEUR=X","TRYEUR=X","TNDEUR=X","THBEUR=X","SZLEUR=X","SOSEUR=X","SLLEUR=X",
"SEKEUR=X","SCREUR=X","SAREUR=X","RWFEUR=X","RUBEUR=X","QAREUR=X","PYGEUR=X","PLNEUR=X","PKREUR=X","PHPEUR=X",
"PGKEUR=X","PENEUR=X","PABEUR=X","OMREUR=X","NZDEUR=X","NPREUR=X","NOKEUR=X","NIOEUR=X","NGNEUR=X","NADEUR=X",
"MYREUR=X","MXNEUR=X","MWKEUR=X","MVREUR=X","MUREUR=X","MOPEUR=X","MMKEUR=X","MKDEUR=X","MGAEUR=X","MDLEUR=X",
"MADEUR=X","LYDEUR=X","LSLEUR=X","LKREUR=X","LBPEUR=X","LAKEUR=X","KZTEUR=X","KWDEUR=X","KRWEUR=X","KMFEUR=X",
"KHREUR=X","KESEUR=X","JPYEUR=X","JODEUR=X","JMDEUR=X","ISKEUR=X","IQDEUR=X","INREUR=X","ILSEUR=X","IDREUR=X",
"HUFEUR=X","HTGEUR=X","HRKEUR=X","HNLEUR=X","HKDEUR=X","GTQEUR=X","GNFEUR=X","GMDEUR=X","GBPEUR=X","EUREUR=X",
"ETBEUR=X","EGPEUR=X","DZDEUR=X","DOPEUR=X","DKKEUR=X","DJFEUR=X","CZKEUR=X","CVEEUR=X","CUPEUR=X","CRCEUR=X",
"COPEUR=X","CNYEUR=X","CLPEUR=X","CHFEUR=X","CADEUR=X","BZDEUR=X","BWPEUR=X","BSDEUR=X","BOBEUR=X","BNDEUR=X",
"BIFEUR=X","BHDEUR=X","BGNEUR=X","BDTEUR=X","BBDEUR=X","AWGEUR=X","AUDEUR=X","ARSEUR=X","ALLEUR=X","AEDEUR=X",
"TWDEUR=X","XOFEUR=X","YERUSD=X","ZARUSD=X"]

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


