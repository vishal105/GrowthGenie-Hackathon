# dashboard.py
import streamlit as st
import markdown as md
import plotly.express as px
import logging
from utilities.CustomerAnalysis import CustomerAnalysis
import pandas as pd


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
    if isinstance(data, pd.DataFrame):
        if len(data.index) > 0:
            st.subheader(header)

def display_account_chart(account_data):
    # Display the pie chart
        st.subheader("Account Balance")
        # Create pie chart for ACCOUNTBALANCE
        account_balance_fig = px.pie(account_data, names='ACCOUNTSTATUS', title='Account Status Distribution',hole=0.4)
        account_balance_fig.update_traces(textposition='auto', textinfo='percent+label')
        st.plotly_chart(account_balance_fig)

def display_investment_dist_chart(user):
    # Merge dataframes to get the total investment amounts for each category
    merged_df = pd.merge(user.fd_data, user.investment_data[['INVESTMENTACCOUNTID', 'INVESTMENTPORTFOLIO']], on='INVESTMENTACCOUNTID', how='left')
    merged_df = pd.merge(merged_df, user.loans_data[['LOANAMOUNT', 'CUSTOMERID']], left_on='CUSTOMERID', right_on='CUSTOMERID', how='left')
    merged_df = pd.merge(merged_df, user.mf_data[['INVESTMENTAMOUNT', 'INVESTMENTACCOUNTID']], left_on='INVESTMENTACCOUNTID', right_on='INVESTMENTACCOUNTID', how='left')
    merged_df = pd.merge(merged_df, user.stocks_data[['PURCHASEPRICE', 'QUANTITY', 'INVESTMENTACCOUNTID']], left_on='INVESTMENTACCOUNTID', right_on='INVESTMENTACCOUNTID', how='left')

    # Calculate total amounts
    total_fd = merged_df['PRINCIPALAMOUNT'].sum()
    total_investment = merged_df['INVESTMENTPORTFOLIO'].sum()
    total_loan = merged_df['LOANAMOUNT'].sum()
    total_mutual_fund = merged_df['INVESTMENTAMOUNT'].sum()
    total_stock = merged_df['PURCHASEPRICE'] * merged_df['QUANTITY']

    # Create a pie chart
    labels = ['FD', 'Investment Portfolio', 'Loan', 'Mutual Fund', 'Stock']
    values = [total_fd, total_investment, total_loan, total_mutual_fund, total_stock.sum()]

    # Include names parameter for labels
    fig = px.pie(names=labels, values=values, title='Investment Distribution',hole=0.4)
    fig.update_traces(textposition='auto', textinfo='percent+label')

    # Display the pie chart using Streamlit
    st.plotly_chart(fig)

# Function to calculate interest income from FDs
def calculate_fd_tax(principal, interest_rate, maturity_amount):
    # Assuming simple interest for simplicity
    interest_earned = maturity_amount - principal

    # Include interest income in total income for tax calculation
    total_income = interest_earned

    # Tax calculation based on income tax slabs for the old regime (as of my last update)
    # You may need to adjust these tax slabs based on the latest regulations
    tax_slabs = [(250000, 0.05), (500000, 0.1), (1000000, 0.2), (10000000, 0.3)]
    tax_paid = 0

    for slab, rate in tax_slabs:
        if total_income > slab:
            tax_paid += (total_income - slab) * rate
            total_income = slab

    return tax_paid

# Function to display the tax calculation results horizontally
def display_tax_results_horizontal(fd_tax_results):
    st.subheader("Tax Calculation Results for FDs (Indian Old Regime)")
    for result in fd_tax_results:   
        st.write(f"FD ID: {result['FD ID']}, Tax Paid: {result['Tax Paid']}")


def display_user_dashboard(usercalled):
    user = CustomerAnalysis(usercalled)
    if len(user.customer_data.index) <= 0:
        st.title("user not found")
    else: 
        customer = user.customer_data
        # Display customer details using the function
        display_customer_details(customer)

        # Tax calculation for each FD
        fd_tax_results = []

        for index, row in user.fd_data.iterrows():
            fd_tax = calculate_fd_tax(row['PRINCIPALAMOUNT'], row['INTERESTRATE'], row['MATURITYAMOUNT'])
            fd_tax_results.append({"FD ID": row['FIXEDDEPOSITID'], "Tax Paid": fd_tax})

        # Display the results horizontally
        display_tax_results_horizontal(fd_tax_results)

        display_account_chart(user.account_data)
        display_investment_dist_chart(user)

        # Display the table in the second column
        display_data(user.account_data, "Account Details")
        display_data(user.fd_data, "FD Details")
        display_data(user.investment_data, "Investment Details")
        display_data(user.loans_data, "Loan Details")
        display_data(user.mf_data, "Mutual Fund Details")
        display_data(user.stocks_data, "Stock Details")
        display_data(user.transactions_data, "Transaction History")
