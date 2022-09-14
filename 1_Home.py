import streamlit as st


st.set_page_config(
    page_title = "Finance Analysis Dashboard",    
    page_icon = "📈",
)
 
st.image('banner.jpg')

st.title("Welcome to our Finance App")
     
#st.sidebar.success("Select a page above.")

st.text("This a simple financila analysis web application built to help you with your \nFundamental Analysis on specific asset.")
st.text("Click on the sidebar menu to access some of the functionalities of our aplication.")



# Removing default footer
hide_st_style = """
                <style>
                footer {visibility: hidden;}
                </style>
                """
st.markdown(hide_st_style, unsafe_allow_html = True)
