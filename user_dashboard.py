# dashboard.py
import streamlit as st
import markdown as md
from utilities.CustomerAnalysis import CustomerAnalysis


PAGE_CONFIG = {"page_title":"Personal Finance", 
            #    "page_icon":image, 
               "layout":"centered", 
               "initial_sidebar_state":"auto"}

st.set_page_config(**PAGE_CONFIG)

st.sidebar.markdown("## Controls")
# sidebar_main = st.sidebar.selectbox('Navigation', ['About the Project', 'EDA', 'Predictions', 'Q&A'])
sidebar_main = st.sidebar.selectbox('Navigation', ['Home', 'Visualisation'])

if sidebar_main == 'Home' : 
    st.title('User Analytics Dashboard')
    st.markdown("""
        ##### User dashboard will give you the details about a particular user 
    """)
    
    # * unable to use direct images due to library issue 
    # st.image('static/compressed_heroimage.gif', caption = 'Personal Finance')
    banner = md.headerSection()
    st.markdown(banner,unsafe_allow_html=True)
    # Add user-specific content here
