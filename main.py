import streamlit as st

st.set_page_config(
     page_title="Arts festival",
     page_icon="ð§",
     layout="wide",
     menu_items={
         'Get Help': 'https://instagram.com/keralauniversitydsu?igshid=YmMyMTA2M2Y=',
         'Report a bug': "https://www.linkedin.com/in/saifudheen-nouphal-2b33a5144/",
         'About': "# Departments union - Campus GALA web app"
     }
 )


import pandas as pd
from registration import athletics
import dataframe_image as dfi
#import gspread as gs
from PIL import Image
import json
import datetime
from data import registration
#from auth import check_password
from union import admin
from data import reg
from registration import register


image= Image.open('ei_1678606707942-removebg-preview.png')

st.image(image)

st.markdown('#  കെട്ട കാലത്തോടുള്ള കലഹത്തിന്റെ കുത്ത്')

st.markdown('#### Departmets Union  ')





#register()
tab1, tab2= st.tabs(["Event Wise Result","Leader Board"])
evn=df['Event'].unique()

with tab1:
     c1,c2=st.columns(2)
     st.markdown('###### Event result')
     option = st.selectbox('',evn,key='event')

          
        
     
