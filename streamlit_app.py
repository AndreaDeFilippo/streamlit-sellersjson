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


title = st.text_input('Company Domain', 'showheroes.com')
