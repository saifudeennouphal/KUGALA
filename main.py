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




def register():
  
  event_name= ['SELECT','Cultural','Sports','Exhibiton']
  departments= ['', 'Department of Aquatic Biology and Fisheries', 'Department of Biochemistry','Department of Botany',
                'Department of Chemistry', 'Department of Demography', 'Department of Geology', 'Department of Mathematics',
                'Department of Physics', 'Department of Psychology' , 'Department of Statistics' , 'Department of Zoology',
                'Department of Arabic', 'Department of Hindi', 'Department of Kerala Studies', 'Department of Linguistics',
                'Department of Malayalam', 'Department of Sanskrit', 'Department of Tamil', 'Oriental Research Institute and Manuscript Library',
                'Department of Biotechnology', 'Department of Computational Biology & Bioinformatics', 'Department of Computer Science' ,
                'Department of Environmental Sciences', 'Department of Futures Studies', 'Department of Nanoscience and Nanotechnology', 
                'Department of Optoelectronics', 'Department of Communication and Journalism', 'Department of German',
                'Department of Library and Information Science', 'Department of Philosophy', 'Department of Russian', 'Institute of English',
                'Department of Archaeology', 'Department of Economics', 'Department of History', 'Department of Islamic and West Asian Studies',
                'Department of Political Science','Department of Sociology', 'Department of Commerce', 'Department of Education',
                'Department of Music', 'Department of Law']
  cul_prog = ['SELECT', 'Solo Dance','Group Dance','Song(Solo)', 'Song(Group)', 'Fashion Show']
  spo_prog = ['SELECT', 'Carroms(Doubles)', '5s Football', 'Badminton(Mixed Doubles)']
  exi_prog = ['SELECT', 'Artwork Exhibition', 'Department Exhition']
  art_exhi = ['SELECT', 'Craft', 'Spot caricature', 'Bottle Art' , 'Others'] 
  slct_evnt= st.selectbox('Select your Event',event_name)
  
  if slct_evnt == "Cultural":
    cprogram = st.selectbox('Select your Programme ',cul_prog)
    cname = st.text_input('Enter your Name :', "")
    cdept = st.selectbox('Select your Department :',departments)
    cphone = st.text_input('Enter your contact number :',"")
  
  if slct_evnt == "Sports":
    sprogram = st.selectbox('Select your Sport ', spo_prog)
    if sprogram == "Carroms(Doubles)": 
      sname = st.text_input('Enter your Name :', "")
      sname2 = st.text_input('Enter the name of your team mate:',"")
      sdept = st.selectbox('Select your Department :',departments)
      sphone = st.text_input('Enter your contact number :',"")
    if sprogram == "5s Football":
      sname = st.text_input('Enter your Name :', "")
      sname1 = st.text_input('Enter the name of your team mate(1)',"")
      sname2 = st.text_input('Enter the name of your team mate(2)',"")
      sname3 = st.text_input('Enter the name of your team mate(3)',"")
      sname4 = st.text_input('Enter the name of your team mate(4)',"")
      sdept = st.selectbox('Select your Department :',departments)
      sphone = st.text_input('Enter your contact number :',"")
    if sprogram == "Badminton(Mixed Doubles)":
      sname = st.text_input('Enter your Name :', "")
      sname2 = st.text_input('Enter the name of your team mate:',"")
      sdept = st.selectbox('Select your Department :',departments)
      sphone = st.text_input('Enter your contact number :',"")
  if slct_evnt == "Exhibiton":
    eprogram = st.selectbox('Select your Programme ',exi_prog)
    if eprogram == "Artwork Exhibition":
      artwork= st.selectbox('Your presentation :',art_exhi)
      if artwork != "Others":
        ename = st.text_input('Enter your Name :', "")
        edept = st.text_input('Enter yout Department:' "")
        ephone = st.text_input('Enter your contact number :',"")
      if artwork == "Others":
        eother = st.text_input('Enter your art work :', "")
        ename = st.text_input('Enter your Name :', "")
        edept = st.text_input('Enter yout Department:' "")
        ephone = st.text_input('Enter your contact number :',"")
    if eprogram == "Department Exhition":
     edept = st.selectbox('Select Department :',departments)
     eexhi = st.text_input('Shortly describe about your exhibition',"")
     


          
        
register()      
