import streamlit as st


st.set_page_config(
    page_title = "Finance Analysis Dashboard",
    page_icon = "👋",
)

st.image('banner.jpg')

st.title("Welcome to our Finance App")

#st.sidebar.success("Select a page above.")

st.text("This a simple financila analysis web application built to help you with your \nFundamental Analysis on specific asset.")
st.text("Click on the sidebar menu to access some of the functionalities of our aplication.")























#st.header(options)
#
#if options == "":
#
#
#if options == "Wealth distribution in Maputo":
#    map_data = pd.DataFrame(
#    np.random.randn(1000, 2) / [50, 50] + [-25.953724, 32.588711],
#    columns=['lat', 'lon'])
#
#    st.map(map_data)
#
#
#
#if options == "crypto":
#	#st.subheader("crypto assets logic")
#	crypto = st.sidebar.text_input('Crypto Symbol', 'Bitcoin', max_chars = 15)
#   # scryptourl = 
#    
#
#if options == "chart":
#    st.subheader("This is the chart dashboard")
#    
#


# Removing default footer
hide_st_style = """
                <style>
                footer {visibility: hidden;}
                </style>
                """
st.markdown(hide_st_style, unsafe_allow_html = True)
