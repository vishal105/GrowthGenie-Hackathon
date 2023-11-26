#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

def data_loader(file_name, **kwargs):
    file_path = r'C:\Users\Akriti Kakkar\Downloads\GrowthGenie-Hackathon-main\GrowthGenie-Hackathon-main\dataset\{}.xlsx'.format(file_name)
    data = pd.read_excel(file_path, **kwargs)
    return data

def sliced_data(data, type):
    sliced_data = data[data['ACCOUNTTYPE'] == type].reset_index(drop=True)
    return sliced_data

def merge_dataframe(df1, df2, on, *args):
    data1 = pd.merge(df1, df2, how='left', on=on)
    data1 = data1[list(args)]
    return data1

def fixed_deposits_manipulation(fixed_deposits1):
    fixed_vol = fixed_deposits1.groupby('FIXEDDEPOSITID', as_index=False).agg({'INVESTMENTACCOUNTID':'count'})
    fixed_vol = fixed_vol.sort_values(by='INVESTMENTACCOUNTID', ascending=False).reset_index(drop=True)
    fixed_vol = fixed_vol.rename(columns={'INVESTMENTACCOUNTID': 'CLIENTCOUNT'})
    fixed_vol1 = pd.merge(fixed_vol, fixed_deposits1, on='FIXEDDEPOSITID', how='left')
    fixed_vol1 = fixed_vol1[['FIXEDDEPOSITID', 'CLIENTCOUNT', 'INTERESTRATE']]
    fixed_vol1 = fixed_vol1.sort_values(by=['INTERESTRATE'], ascending=False).reset_index(drop=True)
    fixed_vol1 = fixed_vol1.drop('CLIENTCOUNT', axis=1)
    fixed_vol1 = fixed_vol1.rename(columns={'FIXEDDEPOSITID': 'Fixed Deposit', 'INTERESTRATE': 'Rate'})
    first_10_entries = fixed_vol1.take([i for i in range(10)])
    return first_10_entries

def mutual_fund_manipulations(mutual_funds1):
    fixed_vol = mutual_funds1.groupby(['MUTUALFUNDID', 'FUNDNAME'], as_index=False).agg({'INVESTMENTACCOUNTID':'count'})
    fixed_vol = fixed_vol.sort_values(by='INVESTMENTACCOUNTID', ascending=False).reset_index(drop=True)
    fixed_vol = fixed_vol.rename(columns={'INVESTMENTACCOUNTID': 'CLIENTCOUNT'})
    fixed_vol1 = pd.merge(fixed_vol, mutual_funds1, on=['MUTUALFUNDID', 'FUNDNAME'], how='left')
    fixed_vol1 = fixed_vol1[['MUTUALFUNDID', 'FUNDNAME', 'CLIENTCOUNT', 'RETURNS']]
    fixed_vol1 = fixed_vol1.sort_values(by=['RETURNS'], ascending=False).reset_index(drop=True)
    fixed_vol1 = fixed_vol1.drop(['CLIENTCOUNT', 'MUTUALFUNDID'], axis=1)
    fixed_vol1 = fixed_vol1.rename(columns={'FUNDNAME': 'Fund Name', 'RETURNS': 'CAGR'})
    first_10_entries = fixed_vol1.take([i for i in range(10)])
    return first_10_entries

def stock_manipulations(stocks1):
    fixed_vol = stocks1.groupby(['STOCKID', 'STOCKNAME'], as_index=False).agg({'INVESTMENTACCOUNTID':'count'})
    fixed_vol = fixed_vol.sort_values(by='INVESTMENTACCOUNTID', ascending=False).reset_index(drop=True)
    fixed_vol = fixed_vol.rename(columns={'INVESTMENTACCOUNTID': 'CLIENTCOUNT'})
    fixed_vol1 = pd.merge(fixed_vol, stocks1, on=['STOCKID', 'STOCKNAME'], how='left')
    fixed_vol1 = fixed_vol1[['STOCKID', 'STOCKNAME', 'CLIENTCOUNT', 'RETURNS']]
    fixed_vol1 = fixed_vol1.sort_values(by=['RETURNS'], ascending=False).reset_index(drop=True)
    fixed_vol1 = fixed_vol1.drop(['CLIENTCOUNT', 'STOCKID'], axis=1)
    fixed_vol1 = fixed_vol1.rename(columns={'STOCKNAME': 'Stock Name', 'RETURNS': 'CAGR'})
    first_10_entries = fixed_vol1.take([i for i in range(10)])
    return first_10_entries

def main():
    accounts = data_loader('accounts', parse_dates=['OPENINGDATE', 'LASTTRANSACTIONDATE'])
    customers = data_loader('customers')
    fixed_deposits = data_loader('fixed_deposits', parse_dates=['MATURITYDATE'])
    mutual_funds = data_loader('mutual_funds', parse_dates=['INVESTMENTDATE'])
    stocks = data_loader('stocks')
    investment_accounts = data_loader('investment_accounts', parse_dates=['INVESTMENTSTARTDATE', 'INVESTMENTENDDATE'])
    fixed_investment = sliced_data(investment_accounts, 'Fixed Deposits')
    fund_investment = sliced_data(investment_accounts, 'Mutual Funds')
    stock_investment = sliced_data(investment_accounts, 'Stocks')
    fixed_deposits1 = merge_dataframe(fixed_deposits, fixed_investment, 'INVESTMENTACCOUNTID',
                                      *['FIXEDDEPOSITID', 'INVESTMENTACCOUNTID', 'INTERESTRATE'])
    mutual_funds1 = merge_dataframe(mutual_funds, fund_investment, 'INVESTMENTACCOUNTID',
                                    *['MUTUALFUNDID', 'FUNDNAME', 'INVESTMENTACCOUNTID', 'RETURNS'])
    stocks1 = merge_dataframe(stocks, stock_investment, 'INVESTMENTACCOUNTID',
                              *['STOCKID', 'STOCKNAME', 'INVESTMENTACCOUNTID', 'RETURNS'])
    final_dataframe = fixed_deposits_manipulation(fixed_deposits1)
    final_dataframe1 = mutual_fund_manipulations(mutual_funds1)
    final_dataframe2 = stock_manipulations(stocks1)
    return final_dataframe, final_dataframe1, final_dataframe2

if __name__ == '__main__':
    final_dataframe, final_dataframe1, final_dataframe2 = main()
    print("Fixed Deposits Manipulation:")
    print(final_dataframe)
    print("\nMutual Fund Manipulations:")
    print(final_dataframe1)
    print("\nStock Manipulations:")
    print(final_dataframe2)


# In[ ]:




