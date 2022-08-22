import streamlit as st
import requests


st.set_page_config(
    page_title = "Stocktwits Sentiment Analysis",
    page_icon = "👋",
)

st.title("Stocktwits")
st.text("Input the symbol of the stock you would like to see the sentiment about on social\nmedia. The sentiment analysis of the stocks is made based on Stocktwits posts \nrelated to a specfic stock of your interest.")
st.text(" eg: AAPL or GOOGL")
Symbol = st.text_input('Symbol', 'AAPL', max_chars = 5)
sturl = requests.get(f'https://api.stocktwits.com/api/2/streams/symbol/{Symbol}.json')
data = sturl.json()
for message in data['messages']:
    st.write(message)
    st.write(message['user']['username'])
    st.image(message['user']['avatar_url'])
    st.write(message['body'])
    st.write(message['created_at'])
           









# Remove default footer
hide_st_style = """
                <style>
                footer {visibility: hidden;}
                </style>
                """
st.markdown(hide_st_style, unsafe_allow_html = True)
