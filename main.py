import streamlit as st

st.set_page_config(
     page_title="ഓണാഘോഷം 2k22",
     page_icon="ð§",
     layout="wide",
     initial_sidebar_state="collapsed",
     menu_items={
         'Get Help': 'https://instagram.com/keralauniversitydsu?igshid=YmMyMTA2M2Y=',
         'Report a bug': "https://www.linkedin.com/in/prabinrajkp18/",
         'About': "# Departments union sports club - campus olympics web app"
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
from auth import check_password
from union import admin
from data import reg







image= Image.open('new logo update.png')

st.image(image)

#image2= Image.open('SFI logo.png')

#st.image(image2)

#st.markdown('#  ഓണാഘോഷം ')

#st.markdown('### ഗവേഷക - ഡിപ്പാർട്മെന്റ്സ് യൂണിയൻ - 2022')

#images = ['newlogo1.png', 'SFI logo.png']
#st.image(images, use_column_width=True, caption="some generic text")







	


	
tab1, tab2 = st.tabs(["Event Wise Result","Leader Board"])

df=athletics()
evn=df['Event'].unique()

with tab1:

	c1,c2=st.columns(2)
	#with c1:
	st.markdown('###### Event result')
	option = st.selectbox('',evn,key='event')

	st.write('Results of ', option)

	ev=df[df['Event']==option]
	ev=ev[['Block','Position']]
			
			
	
	st.dataframe(ev)
	#dfi.export(ev, 'Result.png')
			
	#with open("Result.png", "rb") as file: btn = st.download_button(
				    #label="Download Result",
				    #data=file,
				    #file_name="result.png",
				    #mime="image/png"
				  #)
		
			

		
with tab2:
	
		
			
	st.markdown('###### Leaderboard - Block wise')
	st.dataframe(df.groupby(['Block']).sum()['Point'].reset_index().sort_values(by='Point', ascending=False))
		
		

		
		


	
				
with st.sidebar.expander("Developers"):
	st.markdown('#### [Saifudheen](https://www.instagram.com/saif_udheen/)')
 	st.markdown('#### [Mohammed Ijas S](https://www.instagram.com/ijas.21/)')
	st.markdown('#### [Prabin Raj K P](https://www.instagram.com/prabinraj.kp/)')
	st.markdown('#### [Vijay Venkitesh](https://www.instagram.com/vijay_v_venkitesh/)')
 	st.write('##### Department of Futures Studies')
 	
     #st.image("https://static.streamlit.io/examples/dice.jpg")
			
		
		
	
	
	
	#st.write('ssbsbbs')

#st.dataframe(df)
	
	

