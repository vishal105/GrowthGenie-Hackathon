# customer_analysis.py
import pandas as pd
import streamlit as st
from utilities.AzureSqlLoader import AzureSQLLoader

class CustomerAnalysis:
    def __init__(self,customer_id):
        self.sqlloader = AzureSQLLoader()
        self.customer_id = customer_id
        self.account_data = self.load_data('Accounts',customer_id)
        self.customer_data = self.load_data('Customers',customer_id)
        self.fd_data = self.load_datainv('FixedDeposits',customer_id)
        self.investment_data = self.load_data('InvestmentAccounts',customer_id)
        self.loans_data = self.load_data('Loans',customer_id)
        self.mf_data = self.load_datainv('MutualFunds',customer_id)
        self.stocks_data = self.load_datainv('Stocks',customer_id)
        self.transactions_data = self.load_dataacc('Transactions',customer_id)

        # Filter data based on customer ID
        # Repeat for other datasets

    def load_data(self, file_path,customer_id):
        data = self.sqlloader.load_customer(file_path,customer_id)
        # Additional data validation if needed
        return data
    
    def load_datainv(self, file_path,customer_id):
        data = self.sqlloader.load_customer_join_inv(file_path,customer_id)
        # Additional data validation if needed
        return data
    
    def load_dataacc(self, file_path,customer_id):
        data = self.sqlloader.load_customer_join_acc(file_path,customer_id)
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

        # Repeat for other datasets'
    


