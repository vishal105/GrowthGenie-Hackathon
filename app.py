# dashboard.py
import streamlit as st
import markdown as md
from utilities.CustomerAnalysis import CustomerAnalysis
import pandas as pd
from css import css
from dataframe_visualisation import dataframe_visualisation
import user_dashboard
from dataframe_visualisation import dataframe_visualisation


PAGE_CONFIG = {"page_title":"Personal Finance", 
            #    "page_icon":image, 
               "layout":"centered", 
               "initial_sidebar_state":"auto"}

st.set_page_config(**PAGE_CONFIG)

st.sidebar.markdown("## Controls")
# sidebar_main = st.sidebar.selectbox('Navigation', ['About the Project', 'EDA', 'Predictions', 'Q&A'])
sidebar_main = st.sidebar.selectbox('Navigation', ['Home', 'User Dashboard','Bank Dashboard'])

if sidebar_main == 'Home' : 
    st.title('GrowthGenie App')
    st.markdown("""
        ##### Dashboard will give you the details about a particular user 
    """)
    
    # * unable to use direct images due to library issue 
    # st.image('static/compressed_heroimage.gif', caption = 'Personal Finance')
    banner = md.headerSection()
    st.markdown(banner,unsafe_allow_html=True)
    # Add user-specific content here

if sidebar_main == 'User Dashboard' : 
    st.title('GrowthGenie App')

    st.markdown("""
        ##### Dashboard will give you the details about a particular user 
    """)
    
    user_input = st.text_input("User Details:", "")
    if st.button("Details"):
        try:
            usercalled =  int(user_input)
            user_dashboard.display_user_dashboard(usercalled)
        except:
            st.write("Issue with Input")

if sidebar_main == 'Bank Dashboard' : 
    st.title('GrowthGenie App')

    st.markdown("""
        ##### Dashboard will give you the details about a Bank 
    """)
    
    user_input = st.text_input("Bank Details:", "")
    if st.button("Details"):
        try:
            final_dataframe, final_dataframe1, final_dataframe2, fixed, mutual, stock, new_data, cust_returns, tax_liability = dataframe_visualisation()
            st.table(final_dataframe)
        except:
            st.write("Issue with Input")
