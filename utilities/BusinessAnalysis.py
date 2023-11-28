# customer_analysis.py
import pandas as pd
import streamlit as st
from AzureSqlLoader import AzureSQLLoader

class BusinessAnalysis:
    '''
    
    business = BusinessAnalysis()
    
    '''
    def __init__(self):
        self.sqlloader = AzureSQLLoader()
        self.account_data = self.load_data('Accounts')
        self.customer_data = self.load_data('Customers')
        self.fd_data = self.load_data('FixedDeposits')
        self.investment_data = self.load_data('InvestmentAccounts')
        self.loans_data = self.load_data('Loans')
        self.mf_data = self.load_data('MutualFunds')
        self.stocks_data = self.load_data('Stocks')
        self.transactions_data = self.load_data('Transactions')

    def load_data(self, file_path):
        data = self.sqlloader.load_table(file_path)
        # Additional data validation if needed
        return data
    
    def merge_dataframe(self,data_df1, data_df2, on, *args):
        data1 = pd.merge(data_df1, data_df2, how='left', on=on)
        data1 = data1[list(args)]
        return data1