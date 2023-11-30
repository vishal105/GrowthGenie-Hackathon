# dashboard.py
import streamlit as st
import markdown as md
from utilities.CustomerAnalysis import CustomerAnalysis
import pandas as pd
from css import css


# Function to create Streamlit app for displaying customer account details
def display_customer_details(customer):
    st.subheader("Customer Account Details")

    # Display user data in a nicely formatted way
    col1, col2 = st.columns(2)

    with col1:
        st.write(f'**Customer Id:** {customer["CUSTOMERID"].iloc[0]}')
        st.write(f'**Name:** {customer["FIRSTNAME"].iloc[0]} {customer["LASTNAME"].iloc[0]}')
        st.write(f'**DOB:** {customer["DATEOFBIRTH"].iloc[0]}')

    with col2:
        st.write(f'**Gender:** {map_gender(customer["GENDER"].iloc[0])}')
        st.write(f'**Phone:** {customer["PHONE"].iloc[0].replace(".", "-")}')
        st.write(f'**Email:** {customer["EMAIL"].iloc[0]}')

    st.write(f'**Address:** {customer["ADDRESS"].iloc[0]}')

    # Function to map gender codes to human-readable strings
def map_gender(gender_code):
    if gender_code == 'M':
        return 'Male'
    elif gender_code == 'F':
        return 'Female'
    else:
        return 'Unknown'

def display_data(data, header):
    # if not data.empty:
        st.subheader(header)
        st.write(data)


PAGE_CONFIG = {"page_title":"Personal Finance", 
            #    "page_icon":image, 
               "layout":"centered", 
               "initial_sidebar_state":"auto"}

st.set_page_config(**PAGE_CONFIG)

st.sidebar.markdown("## Controls")
# sidebar_main = st.sidebar.selectbox('Navigation', ['About the Project', 'EDA', 'Predictions', 'Q&A'])
sidebar_main = st.sidebar.selectbox('Navigation', ['Home', 'User Dashboard','Business Visualisation'])

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
            user = CustomerAnalysis(usercalled)
            customer = user.customer_data
            # Display customer details using the function
            display_customer_details(customer)
            display_data(user.account_data, "Account Details")
            display_data(user.fd_data, "FD Details")
            display_data(user.investment_data, "Investment Details")
            display_data(user.loans_data, "Loan Details")
            display_data(user.mf_data, "Mutual Fund Details")
            display_data(user.stocks_data, "Stock Details")
            display_data(user.transactions_data, "Transaction History")
        
            
        
            
        except:
            st.write("Issue with Input")
