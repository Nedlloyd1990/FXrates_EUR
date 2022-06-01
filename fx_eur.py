import streamlit as st
from yahoofinancials import YahooFinancials
import pandas as pd
from datetime import datetime
import numpy as np
import os



currentDate=datetime.today().strftime('%Y-%m-%d')

currencies = ["SGDEUR=X","USDEUR=X","GBPEUR=X"]

dict1={}


#st.sidebar.multiselect("select something", ["USDZAR=X","USDYER=X","USDXPF=X","USDXOF=X","USDXCD=X","USDXAF=X","USDVND=X","USDUZS=X","USDUYU=X","USDUGX=X","USDUAH=X","USDTZS=X","USDTTD=X","USDTRY=X","USDTND=X","USDTHB=X","USDSZL=X","USDSOS=X","USDSLL=X","USDSEK=X","USDSCR=X","USDSAR=X","USDRWF=X","USDRUB=X","USDQAR=X","USDPYG=X","USDPLN=X","USDPKR=X","USDPHP=X","USDPGK=X","USDPEN=X","USDPAB=X","USDOMR=X","USDNZD=X","USDNPR=X","USDNOK=X","USDNIO=X","USDNGN=X","USDNAD=X","USDMYR=X","USDMXN=X","USDMWK=X","USDMVR=X","USDMUR=X","USDMOP=X","USDMMK=X","USDMKD=X","USDMGA=X","USDMDL=X","USDMAD=X","USDLYD=X","USDLSL=X","USDLKR=X","USDLBP=X","USDLAK=X","USDKZT=X","USDKWD=X","USDKRW=X","USDKMF=X","USDKHR=X","USDKES=X","USDJPY=X","USDJOD=X","USDJMD=X","USDISK=X","USDIQD=X","USDINR=X","USDILS=X","USDIDR=X","USDHUF=X","USDHTG=X","USDHRK=X","USDHNL=X","USDHKD=X","USDGTQ=X","USDGNF=X","USDGMD=X","USDGBP=X","USDEUR=X","USDETB=X","USDEGP=X","USDDZD=X","USDDOP=X","USDDKK=X","USDDJF=X","USDCZK=X","USDCVE=X","USDCUP=X","USDCRC=X","USDCOP=X","USDCNY=X","USDCLP=X","USDCHF=X","USDCAD=X","USDBZD=X","USDBWP=X","USDBSD=X","USDBOB=X","USDBND=X","USDBIF=X","USDBHD=X","USDBGN=X","USDBDT=X","USDBBD=X","USDAWG=X","USDAUD=X","USDARS=X","USDALL=X","USDAED=X","USDTWD=X","USDSGD=X"],["USDZAR=X","USDYER=X","USDXPF=X","USDXOF=X","USDXCD=X","USDXAF=X","USDVND=X","USDUZS=X","USDUYU=X","USDUGX=X","USDUAH=X","USDTZS=X","USDTTD=X","USDTRY=X","USDTND=X","USDTHB=X","USDSZL=X","USDSOS=X","USDSLL=X","USDSEK=X","USDSCR=X","USDSAR=X","USDRWF=X","USDRUB=X","USDQAR=X","USDPYG=X","USDPLN=X","USDPKR=X","USDPHP=X","USDPGK=X","USDPEN=X","USDPAB=X","USDOMR=X","USDNZD=X","USDNPR=X","USDNOK=X","USDNIO=X","USDNGN=X","USDNAD=X","USDMYR=X","USDMXN=X","USDMWK=X","USDMVR=X","USDMUR=X","USDMOP=X","USDMMK=X","USDMKD=X","USDMGA=X","USDMDL=X","USDMAD=X","USDLYD=X","USDLSL=X","USDLKR=X","USDLBP=X","USDLAK=X","USDKZT=X","USDKWD=X","USDKRW=X","USDKMF=X","USDKHR=X","USDKES=X","USDJPY=X","USDJOD=X","USDJMD=X","USDISK=X","USDIQD=X","USDINR=X","USDILS=X","USDIDR=X","USDHUF=X","USDHTG=X","USDHRK=X","USDHNL=X","USDHKD=X","USDGTQ=X","USDGNF=X","USDGMD=X","USDGBP=X","USDEUR=X","USDETB=X","USDEGP=X","USDDZD=X","USDDOP=X","USDDKK=X","USDDJF=X","USDCZK=X","USDCVE=X","USDCUP=X","USDCRC=X","USDCOP=X","USDCNY=X","USDCLP=X","USDCHF=X","USDCAD=X","USDBZD=X","USDBWP=X","USDBSD=X","USDBOB=X","USDBND=X","USDBIF=X","USDBHD=X","USDBGN=X","USDBDT=X","USDBBD=X","USDAWG=X","USDAUD=X","USDARS=X","USDALL=X","USDAED=X","USDTWD=X","USDSGD=X"])

yahoo_financials_currencies = YahooFinancials(currencies)
data=yahoo_financials_currencies.get_historical_price_data("2005-01-01", str(currentDate), "daily")

pdd=pd.DataFrame(data)


for ccy in currencies:
	filter1= pdd[str(ccy)]['prices']
	filter2=pd.DataFrame(filter1).close
	dict1[ccy]=filter2
	#print("load")

converttime=pd.DataFrame(filter1).formatted_date
dict1['Date']=converttime


d1=pd.DataFrame(dict1, columns=dict1.keys())
column_to_move = d1.pop("Date")
d1.insert(0, "Date", column_to_move)



@st.cache
def convert_df(df):
   return df.to_csv().encode('utf-8')


csv = convert_df(d1)


st.dataframe(d1)
#st.download_button(label='Download Current Result',   data=d1 , file_name= 'df_test.xlsx')
st.download_button( "Click to Download", csv, "file.csv",  "text/csv",   key='download-csv')
