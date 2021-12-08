import streamlit as st
import pandas as pd
import numpy as np
import requests
import tweepy
import time


st.image('PFF_Logo_WP.png')



#-25.953724, and the longitude is 32.588711




options = st.sidebar.selectbox("Which Dashboard: ",("stocktwits","Wealth distribution in Maputo", "crypto", "wallstreetbets",
                                                    "chart", "pattern", 
                                                    ))

st.header(options)

#if options == "twitter":
#    st.subheader("twitter dashboard logic")

if options == "stocktwits":
    Symbol = st.sidebar.text_input('Symbol', 'AAPL', max_chars = 5)
    sturl = requests.get(f'https://api.stocktwits.com/api/2/streams/symbol/{Symbol}.json')
    data = sturl.json()
    for message in data['messages']:
        #st.write(message)
        st.write(message['user']['username'])
        st.image(message['user']['avatar_url'])
        st.write(message['body'])
        st.write(message['created_at'])
           

if options == "Wealth distribution in Maputo":
    map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [-25.953724, 32.588711],
    columns=['lat', 'lon'])

    st.map(map_data)



if options == "crypto":
	#st.subheader("crypto assets logic")
	crypto = st.sidebar.text_input('Crypto Symbol', 'Bitcoin', max_chars = 15)
   # scryptourl = 
    

if options == "chart":
    st.subheader("This is the chart dashboard")
    
