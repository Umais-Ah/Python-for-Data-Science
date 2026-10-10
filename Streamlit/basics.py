import streamlit as st
import pandas as pd
import time 
#text utility

st.title ('Startup Dashboard')

st.header('I am learning Streamlit')

st.subheader('And I am loving it!')

st.write('This is a normal text')

st.markdown("""
### My favorite movies
- Race 3
- Humshakals
- Housefull
""")

st.code("""
def foo(input):
        return foo**2

x=foo(2)
""")

st.latex('x^2 + y^2 + 2=0')


df=pd.DataFrame({
    'name':['Nitish','Ali','Ahmed'],
    'marks':[50,60,70],
    'package':[10,12,14]
})

st.dataframe(df)

st.metric('Revenue','Rs 3L','-3%')

st.json({
    'name':['Nitish','Ali','Ahmed'],
    'marks':[50,60,70],
    'package':[10,12,14]
})
#----Displaying Media 

st.image('pic.png')
# st.video(#video name)

#----Creating layouts 

st.sidebar.title('Sidebar title')

col1,col2= st.columns(2)

with col1:
    st.image('pic.png')
    
with col2:
    st.image('pic.png')

#---Showing Status 

st.error('Login Failed')
st.success('Login Sucessfull')
st.info('Login Sucessfull')
st.warning('Login Sucessfull')

bar =st.progress(0)

for i in range(1,101):
    time.sleep(0.1)
    bar.progress(i)

#-----------------Taking user input 

email=st.text_input('Enter email')
number=st.number_input('Enter age')
date=st.date_input('Enter regis date')

#Login page

email=st.text_input('Enter email')
password=st.text_input('Enter password')
gender=st.selectbox('select gender',['male','female','others'])


btn = st.button('Login')

#if button is clicked
if btn:
    if email=='umais@gmail.com' and password=='1234':
        # st.success('Login sucessfull')
        st.balloons()
        st.write(gender)
    else:
        st.error('Login fail')

#---file
file=st.file_uploader('upload a csv file')

if file is not None:
    df=pd.read_csv(file)
    st.dataframe(df.describe())
