import streamlit as st
import pandas as pd
import numpy as np
import requests
import tweepy
from bs4 import BeautifulSoup
import time
import requests


st.image('PFF_Logo_WP.png')



options = st.sidebar.selectbox("Which Dashboard: ",("","stocktwits sentiment analysis",
                                                    "Wealth distribution in Maputo", "crypto", 
                                                    "wallstreetbets", "chart", "pattern",))

st.header(options)

if options == "":
    st.title("Welcome to our Finance App")
    st.text("This a simple finance web application that was built to help you study the sentiment")
    st.text("around a specific asset around the world.")
    st.text("Click on the sidebar menu to access some of the functionalities of our aplication.")


if options == "stocktwits sentiment analysis":
    st.text("Input the symbol of the stock you would like to se the social sentiment about,")
    st.text("The sentiment analysis of the stocks is made based on Stocktwits posts related to")
    st.text("a specfic tock of interest")
    st.text(" eg: AAPL or GOOGL")
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
    
