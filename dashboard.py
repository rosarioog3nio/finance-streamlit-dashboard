import streamlit as st
import pandas as pd
import numpy as np
import requests
import tweepy

#st.image('/home/mr-g3tl3m4n/CandleStickPlot.png')

options = st.sidebar.selectbox("Which Dashboard: ",( "twitter", "wallstreetbets",
                                                         "stocktwits", "chart", "pattern"))

st.header(options)

if options == "stocktwits":
    Symbol = st.sidebar.text_input('Symbol', 'AAPL', max_chars = 5)
    r = requests.get(f'https://api.stocktwits.com/api/2/streams/symbol/{Symbol}.json')
    data = r.json()
    
if options == "crypto":
	#st.subheader("crypto assets logic")
	crypto = st.sidebar.text_input('Crypto Symbol', 'Bitcoin', max_chars = 15)
   # scryptourl =     


if options == "twitter":
    st.subheader("twitter dashboard logic")

if options == "chart":
    st.subheader("This is the chart dashboard")



    
    for message in data['messages']:
        #st.write(message)
        st.write(message['user']['username'])
        st.image(message['user']['avatar_url'])
        st.write(message['body'])
        st.write(message['created_at'])
        
        
        

