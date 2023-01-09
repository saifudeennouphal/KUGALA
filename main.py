import streamlit as st

st.set_page_config(
     page_title="Campus Gala",
     page_icon="ð§",
     layout="wide",
     menu_items={
         'Get Help': 'https://instagram.com/keralauniversitydsu?igshid=YmMyMTA2M2Y=',
         'Report a bug': "https://www.linkedin.com/in/saifudheen-nouphal-2b33a5144/",
         'About': "# Departments union - Campus GALA web app"
     }
 )


import pandas as pd
from data import athletics
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


image= Image.open('LOGO-01.png')

st.image(image)

st.markdown('#  Campus GALA')

st.markdown('#### Departmets Union | Researchers Union ')


register()
