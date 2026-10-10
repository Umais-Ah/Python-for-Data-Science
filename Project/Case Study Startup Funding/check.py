import streamlit as st 
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(layout='wide',page_title='StartUp Analysis')

def clean_display(df):
    return df.fillna({
        'investors': 'Not Disclosed',
        'amount': 'Not Disclosed',
        'industry': 'Unknown',
        'sector': 'Unknown',
        'date': 'Unknown',
        'location': 'Unknown'
    })

df=pd.read_csv('startup_clean.csv')
st.sidebar.title('Startup Funding Analysis')
option=st.sidebar.selectbox('Select One',['Overall Analysis','Startup','Investor'])


def load_investor_details(investor):
    st.title(selected_investor)
    
    #latest 5 investment
    last_5_df=df[df['investors'].str.contains(investor, na=False)].sort_values('date',ascending=False).head()
    last_5_df=clean_display(last_5_df)
    st.subheader('Most Recent Invesments')
    st.dataframe(last_5_df)
    
    col1,col2=st.columns(2)
    

    #Biggest investments
    with col1:
        bamount_series=df[df['investors'].str.contains(selected_investor, na=False)].groupby('startup')['amount'].sum().replace(0.0,np.nan).sort_values(ascending=False)
        bamount_series=clean_display(bamount_series)
        st.subheader('Biggest Investments')
        fig, ax = plt.subplots()
        ax.bar(bamount_series.index,bamount_series.values)
        st.pyplot(fig)
    with col2:
        vertical_series=df[df['investors'].str.contains(investor, na=False)].groupby('industry')['amount'].sum()
        st.subheader('Sectors investment in')
        fig, ax = plt.subplots()
        ax.pie(vertical_series,labels=vertical_series.index)
        st.pyplot(fig)






if option=='Overall':
    st.title('Overall Analysis')
elif option=='Startup':
    selected_startup=st.sidebar.selectbox('Select StartUp',sorted(df['startup'].unique().tolist()))
    btn1=st.sidebar.button('Find StartUp Details')
    if btn1:
        st.title(selected_startup)
    


elif option=='Investor':
    selected_investor=st.sidebar.selectbox('Select Investor',sorted(set(df['investors'].dropna().str.split(',').explode().str.strip())))
    btn2=st.sidebar.button('Find Investor Details')
    if btn2:
        load_investor_details(selected_investor)
    

