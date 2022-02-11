import pandas as pd
import sqlalchemy as sa
from sqlalchemy.types import DateTime,VARCHAR,Integer,Date,Float
import requests
import numpy as np
import dataframe_image as dfi
from datetime import datetime
import lxml
import os
#proxy = '*'

os.environ['http_proxy'] = proxy 
os.environ['HTTP_PROXY'] = proxy
os.environ['https_proxy'] = proxy
os.environ['HTTPS_PROXY'] = proxy
engine = sa.create_engine('mssql+pyodbc://*')
engine2 = sa.create_engine('mssql+pyodbc://*')

#Query
ds1 = '''your query'''
ds2 = '''your query'''
#Append dataframe
df1 = pd.read_sql_query(ds1, con=engine)
df2 = pd.read_sql_query(ds2, con=engine)
print("LOADED")
df=pd.DataFrame()
df = df1.append(df,ignore_index=True)
df = df2.append(df,ignore_index=True)
df=df[['source_table','CHANNEL','tanggal']]

#tanggal dan export image
dfi.export(df,"mytable.png",table_conversion='matplotlib')
tanggal = datetime.today().strftime('%Y-%m-%d')

#send to telegram channel
TOKEN = "*"
offset = 0
baseURL = "https://api.telegram.org/bot" + TOKEN
payload = {'chat_id':'*','caption':"update tanggal: "+str(tanggal) }
files = {'photo':open('mytable.png','rb') }
resp = requests.post(baseURL+"/sendPhoto", files=files,data=payload)
print(resp.status_code)