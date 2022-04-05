import requests
import pandas as pd
import streamlit as st
from PIL import Image
from io import BytesIO

# Header

response = requests.get('https://raw.githubusercontent.com/AndreaDeFilippo/icons/main/company/Logo-header_2.png')
image = Image.open(BytesIO(response.content))
st.image(image)

st.title('SellersJson to CSV Tool')



st.subheader('Insert Company URL')
st.warning("Don't put http:// and/or www in the field.")
title = st.text_input('Domain', 'showheroes.com')

url = "https://us-central1-viralize-gateway.cloudfunctions.net/mergeSellers?providers=" + title
df = pd.read_json(url, lines=True)


rename = {'seller_id' : 'Seller ID',
          'name' : 'Name',
          'domain' : 'Domain',
          'seller_type' : 'Seller Type',
          'provider' : 'Player'}

df = df.rename(columns=rename)

columns = ['Player', 'Seller ID', 'Domain', 'Seller Type', 'Name']

df = df[columns]

st.dataframe(df)

@st.cache
def convert_df(df):
          # IMPORTANT: Cache the conversion to prevent computation on every rerun
          return df.to_csv().encode('utf-8')

csv = convert_df(df)

st.download_button(
     label="Download as CSV",
     data=csv,
     file_name= title + '-sellers.csv',
     mime='text/csv',
 )
