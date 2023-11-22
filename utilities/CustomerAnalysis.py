# customer_analysis.py
import pandas as pd
import streamlit as st

class CustomerAnalysis:
    def __init__(self, customer_id):
        self.customer_id = customer_id
        self.account_data = self.load_data('account.xlsx')
        self.customer_data = self.load_data('customer.xlsx')
        self.fd_data = self.load_data('fixed_deposit.xlsx')
        self.investment_data = self.load_data('investment_accounts.xlsx')
        self.loans_data = self.load_data('loans.xlsx')
        self.mf_data = self.load_data('mutual_funds.xlsx')
        self.stocks_data = self.load_data('stocks.xlsx')
        self.transactions_data = self.load_data('transactions.xlsx')

        # Filter data based on customer ID
        self.customer_accounts = self.filter_customer_data(self.account_data, 'Account_ID')
        self.customer_loans = self.filter_customer_data(self.loans_data, 'Customer_ID')
        # Repeat for other datasets

    def load_data(self, file_path):
        data = pd.read_excel(file_path)
        # Additional data validation if needed
        return data

    def filter_customer_data(self, data, id_column):
        return data[data[id_column] == self.customer_id]

    def display_customer_analysis(self):
        # Display customer information
        st.header('Customer Information')
        st.write(self.customer_data[self.customer_data['Customer_ID'] == self.customer_id])

        # Display accounts
        st.header('Customer Accounts')
        st.write(self.customer_accounts)

        # Display loans
        st.header('Customer Loans')
        st.write(self.customer_loans)

        # Repeat for other datasets
