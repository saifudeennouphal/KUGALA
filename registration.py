import streamlit as st
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
  slct_evnt= st.selectbox('Select your Event',event_name)
  
  if event_name == "Cultural":
    cprogram = st.selectbox('Select your Programme ',cul_prog)
    cname = st.text_input('Enter your Name :', "")
    cdept = st.selectbox('Select your Department :',departments)
    cphone = st.text_input('Enter your contact number :',"")
  
  if event_name == "Sports":
    sprogram = st.selectbox('Select your Sport ', spo_prog)
    cname = st.text_input('Enter your Name :', "")
    cdept = st.selectbox('Select your Department :',departments)
    cphone = st.text_input('Enter your contact number :',"")
    
  
    
