"""
import streamlit as st

st.set_page_config(
     page_title="ഓണാഘോഷം 2k22",
     page_icon="ð§",
     layout="wide",
     initial_sidebar_state="expanded",
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







	


	
tab1, tab2 , tab3 = st.tabs(["Leader Board","Gallery","Event Wise Result"])

df=athletics()
evn=df['Event'].unique()


		
			

		
with tab1:
	
		
			
	st.markdown('###### Leaderboard - Block wise')
	st.dataframe(df.groupby(['Block']).sum()['Point'].reset_index().sort_values(by='Point', ascending=False))

with tab2:
	
	img=['anashwara.jpeg','WhatsApp Image 2022-08-24 at 8.54.26 AM.jpeg','WhatsApp Image 2022-08-24 at 8.54.28 AM.jpeg','WhatsApp Image 2022-08-24 at 8.54.29 AM (1).jpeg',
	     'WhatsApp Image 2022-08-24 at 8.54.29 AM.jpeg','WhatsApp Image 2022-08-24 at 8.54.30 AM (1).jpeg',
	     'WhatsApp Image 2022-08-24 at 8.54.30 AM.jpeg','WhatsApp Image 2022-08-25 at 10.36.30 AM.jpeg',
	     'WhatsApp Image 2022-08-25 at 10.36.33 AM.jpeg','WhatsApp Image 2022-08-25 at 10.36.35 AM.jpeg',
	     'WhatsApp Image 2022-08-25 at 10.36.37 AM.jpeg','WhatsApp Image 2022-08-25 at 10.36.51 AM.jpeg',
	     'WhatsApp Image 2022-08-25 at 10.37.14 AM.jpeg','WhatsApp Image 2022-08-25 at 10.37.16 AM.jpeg',
	     'WhatsApp Image 2022-08-27 at 9.18.02 AM.jpeg','WhatsApp Image 2022-08-27 at 9.18.03 AM (1).jpeg',
	     'WhatsApp Image 2022-08-27 at 9.18.04 AM (1).jpeg','WhatsApp Image 2022-08-27 at 9.18.04 AM.jpeg',
	     'WhatsApp Image 2022-08-27 at 9.18.05 AM.jpeg',
	     'WhatsApp Image 2022-08-27 at 9.18.06 AM.jpeg','WhatsApp Image 2022-08-27 at 9.18.07 AM (1).jpeg',
	     'WhatsApp Image 2022-08-27 at 9.18.07 AM.jpeg','WhatsApp Image 2022-08-27 at 9.18.08 AM (1).jpeg',
	     'WhatsApp Image 2022-08-27 at 9.18.08 AM.jpeg']
	st.image(img)
	
with tab3:

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
		
		

		
		


	
				
with st.sidebar.expander("Developers"):
	st.markdown('#### [Mohammed Ijas S](https://www.instagram.com/ijas.21/)')
	st.markdown('#### [Saifudheen](https://www.instagram.com/saif_udheen/)')
	st.markdown('#### [Prabin Raj K P](https://www.instagram.com/prabinraj.kp/)')
	st.markdown('#### [Vijay Venkitesh](https://www.instagram.com/vijay_v_venkitesh/)')
	st.markdown('#### [Mohammed Nibin](https://www.instagram.com/_nibin_/)')
	
 	#st.write('##### Department of Futures Studies')
 	
     #st.image("https://static.streamlit.io/examples/dice.jpg")
			
		
		
	
	
	
	#st.write('ssbsbbs')

#st.dataframe(df)
"""
	
	
import streamlit as st

st.set_page_config(
     page_title="Campus olympics",
     page_icon="ð§",
     layout="wide",
     initial_sidebar_state="expanded",
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







image= Image.open('logo.png')

st.image(image)

st.markdown('#  Campus olympics')

st.markdown('#### Departmets Union Sports Club')






st.write('---')

c=check_password()

if c==True:
	
	admin()

else:
	
	


	tab1, tab2,tab3 = st.tabs(["Event Wise Result","Leader Board","Registration"])

	df=athletics()
	evn=df['Event'].unique()

	with tab1:

		c1,c2=st.columns(2)
		#with c1:
		st.markdown('###### Event result')
		option = st.selectbox('',evn,key='event')

		st.write('Results For ', option)

		ev=df[df['Event']==option]
		ev=ev[['Name','Faculty','Department','Position']]
			
			
		bd=ev.style.set_properties(**{'background-color': 'black',
				                   'color': 'white',
				                   'border-color': 'Red'}).hide_index().set_caption(str(option)+' result')
			
		st.dataframe(ev)
		#dfi.export(ev, 'Result.png')
			
		#with open("Result.png", "rb") as file: btn = st.download_button(
				     #label="Download Result",
				     #data=file,
				     #file_name="result.png",
				     #mime="image/png"
				   #)
		st.write('---')	       
		#with c2:
		st.markdown('###### Leaderboard - Individual')
		dpt=df[df['Department']!='']
		dpt=dpt.groupby(['Name']).sum()['Points'].reset_index().sort_values(by='Points', ascending=False).head(10)
		st.dataframe(dpt)
			

		
	with tab2:
		c1,c2=st.columns(2)
		
		with c1:
		
			
			st.markdown('###### Leaderboard - Faculty wise')
			st.dataframe(df.groupby(['Faculty']).sum()['Points'].reset_index().sort_values(by='Points', ascending=False))
		
		with c2:
			st.markdown('###### Leaderboard - Department wise')
			dpt=df.groupby(['Department']).sum()['Points'].reset_index().sort_values(by='Points', ascending=False)
			dpt=dpt.head(10)
			st.dataframe(dpt[dpt['Department']!=''])

		
		


	with tab3:

		#name,mob,mail= None
		with st.form("reg", clear_on_submit=True):
			tb1,tb2=st.columns(2)
		
			#st.write('name')
			with tb1:
				name=st.text_input(label='Name')
				mob=st.text_input(label='Phone')
				mail=st.text_input(label='E-mail')
			with tb2:
				gen=st.selectbox('Gender',('Male','Female','Transgender'))
				d = st.date_input( "Date of birt",datetime.date(1999, 1, 1))
				
				fac=st.selectbox('Faculty',
				('Applied Science and Technology','Arts, Education & Music','IMk, Commerce & Law','OrientalStudies','Science','Social Science'))
			
			items = st.multiselect(
		 'Events (Maximum 3 events)',
		 ['100 meter','200 meter','400 meter','1500 meter','Walking (3000 meter)','Shot put','Discus Throw','Javelin throw','Cricket Ball Throw'])
			
			
			submit_button = st.form_submit_button(label='Submit')
		#st.write(len(name),len(mob),len(mail))
		
		
			
		if len(items)>3 and submit_button==True:
			st.error('Error: items cannot be more than 3')
		#st.write(name,mob,mail,fac)
		elif submit_button==True and ((len(name) and len(mob) and len(mail))<1)  :
			st.error("Error: all fields must be filled")
			
		elif submit_button==True:
			st.success(str(name)+' Successfully registered for ' + str(items))
			
			for event in items:
				
				lst=[name,mob,mail,gen,fac,str(d),event]
				registration(lst)
				
with st.sidebar.expander("Developers"):
 	st.markdown('#### [Prabin Raj K P](https://www.linkedin.com/in/prabinrajkp18/)')
 	st.markdown('#### [Vijay V Venkitesh](https://www.linkedin.com/in/vijay-v-venkitesh-673177204/)')
 	st.write('##### MSc Data Science \n Department of Futures Studies')
 	
     #st.image("https://static.streamlit.io/examples/dice.jpg")
			
		
		
	
	
	
	#st.write('ssbsbbs')

#st.dataframe(df)

