import streamlit as st
import json
import pandas as pd
import gspread as gs
import os




def registration(lst,sheet):

	j=st.secrets['js']
	res = json.loads(j)
	with open('data.json', 'w') as f:
		json.dump(res, f)

	gc = gs.service_account(filename='data.json')
	os.remove('data.json')
	
	sh = gc.open_by_url(st.secrets['reg'])
	ws = sh.worksheet(sheet)
	
	ws.insert_row(lst,2)
	
	#return None
  
  

def register():
  with st.form("registration1"):
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
                'Department of Music', 'Department of Law','Institute of Management in Kerala']
    cul_prog = ['SELECT', 'Solo Dance','Group Dance', 'Classical Dance' ,'Song(Solo)', 'Song(Group)', 'Classical Music','Musical Instruments', 'Fashion Show']
    spo_prog = ['SELECT', 'Carroms(Doubles)', '5s Football', 'Badminton(Mixed Doubles)']
    exi_prog = ['SELECT', 'Artwork Exhibition', 'Department Exhibition']
    art_exhi = ['SELECT', 'Craft', 'Spot caricature', 'Bottle Art' , 'Others'] 
    
    slct_evnt= st.selectbox('Select your Event',event_name)
    button=st.form_submit_button('Next')
    if button ==True and slct_evnt == "SELECT":
      st.markdown('##### Please select event!')  
    if slct_evnt == "Cultural":
      st.error('Sorry.. Registration for Cultural Program is Closed')
      #st.success = st.selectbox('Select your Programme ',cul_prog) 
      #cname = st.text_input('Enter your Name :', "")
      #cdept = st.selectbox('Select your Department :',departments)
      #cphone = st.text_input('Enter your contact number :',"")
      #citem = st.text_input('For classical dance/ Musical instruments please specify',"")
      #button=st.form_submit_button('Submit')
      #if button == True and cname=="" or cdept=="" or cphone=="" or citem=="SELECT" or cprogram=="SELECT":
        #st.markdown('##### Please enter complete details!')
      #else:
        #st.success('Hello you have successfully registered..')
        #lst=[cname,cdept,cphone,cprogram,citem]
        #registration(lst,'Sheet1')

    if slct_evnt == "Sports":
      sprogram = st.selectbox('Select your Sport ', spo_prog)
      button=st.form_submit_button('Next ')
      if button ==True and slct_evnt == "SELECT":
        st.markdown('##### Please select event!')        
      
      if sprogram == "Carroms(Doubles)": 
        sname = st.text_input('Enter your Name :', "")
        sname2 = st.text_input('Enter the name of your team mate:',"")
        sdept = st.selectbox('Select your Department :',departments)
        sphone = st.text_input('Enter your contact number :',"")
        button=st.form_submit_button('Submit')
        if button == True and sname=="" or sdept=="" or sphone=="" or sprogram=="SELECT":
          st.markdown('##### Please enter complete details!')  
        else:
          st.success('Hello you have successfully registered..')
          lst=[sname,sname2,sdept,sphone,'Carroms']
          registration(lst,'Sheet2')
        
      if sprogram == "5s Football":
        sname = st.text_input('Enter your Name :', "")
        sname1 = st.text_input('Enter the name of your team mate(1)',"")
        sname2 = st.text_input('Enter the name of your team mate(2)',"")
        sname3 = st.text_input('Enter the name of your team mate(3)',"")
        sname4 = st.text_input('Enter the name of your team mate(4)',"")
        sname5 = st.text_input('Enter the name of your team mate(5)',"")
        sname6 = st.text_input('Enter the name of your team mate(6)',"")
        sphone = st.text_input('Enter your contact number :',"")
        button=st.form_submit_button('Submit')
        if button == True and sname==""  or sphone=="" or sprogram=="SELECT":
          st.markdown('##### Please enter complete details!') 
        else:
          st.success('Hello you have successfully registered..')
          lst=[sname,sname1,sname2,sname3,sname4,sname5,sname6,sphone,'5s Football']
          registration(lst,'Sheet3')
          
      if sprogram == "Badminton(Mixed Doubles)":
        sname = st.text_input('Enter your Name :', "")
        sname2 = st.text_input('Enter the name of your team mate:',"")
        sdept = st.selectbox('Select your Department :',departments)
        sphone = st.text_input('Enter your contact number :',"")
        button=st.form_submit_button('Submit')
        if button == True and sname=="" or sdept=="" or sphone=="" or sprogram=="SELECT":
          st.markdown('##### Please enter complete details!')
        else:
          st.success('Hello you have successfully registered..')
          lst=[sname,sname2,sdept,sphone,sprogram]
          registration(lst,'Sheet4')
          
    if slct_evnt == "Exhibiton":
      eprogram = st.selectbox('Select your Programme ',exi_prog)
      button=st.form_submit_button('Next ')
      if eprogram == "Artwork Exhibition":
        artwork= st.selectbox('Your presentation :',art_exhi)
        ename = st.text_input('Enter your Name :', "")
        edept = st.text_input('Enter yout Department:' "")
        ephone = st.text_input('Enter your contact number :',"")
        eothers = st.text_area('If others, Please specify')
        button=st.form_submit_button('Submit')
        if button == True and ename=="" or edept=="" or ephone=="" or eprogram=="SELECT" or artwork=="SELECT":
          st.markdown('##### Please enter complete details!')
        else:
          st.success('Hello you have successfully registered..')
          lst=[artwork,ename,edept,ephone,eothers]
          registration(lst,'Sheet5')
	
      if eprogram == "Department Exhibition":
        ename= st.text_input('Enter your Name:',"")
        edept = st.selectbox('Select Department :',departments)
        eexhi = st.text_area('Shortly describe about your exhibition',"")
        button=st.form_submit_button('Submit')
        if button == True and edept=="" or eexhi=="" or ename=="" or eprogram=="SELECT" :
          st.markdown('##### Please enter complete details!')
        else:
          st.success('Hello you have successfully registered..')
          lst=[ename,edept,eexhi,eprogram]
          registration(lst,'Sheet6')
    
    
