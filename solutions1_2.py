#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import warnings
warnings.filterwarnings('ignore')

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
    mutual_funds1['FUNDNAME.1'] = mutual_funds1['FUNDNAME'].values + ' ' + mutual_funds1['FUNDTYPE'].values
    mutual_funds1 = mutual_funds1.drop('FUNDNAME', axis = 1)
    mutual_funds1 = mutual_funds1.rename(columns = {'FUNDNAME.1' : 'FUNDNAME'})
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

# solution 2 top 3 performining investment to be shown for both user and bank in the form of 3 cards,
# 3 rows segmenting each type

def manipulations_sol2(fixed_deposits_sol2, mutual_funds_sol2, stocks_sol2):
    fixed_deposits_frame = fixed_deposits_sol2.dropna()
    fixed_deposits_frame['FIXEDDEPOSITID'] = fixed_deposits_frame['FIXEDDEPOSITID'].astype(int)
    fixed_deposits_frame = fixed_deposits_frame.drop('INVESTMENTACCOUNTID', axis = 1)
    fixed_deposits_frame = fixed_deposits_frame.sort_values(by = 'RETURNS', ascending = False).reset_index(drop = True)
    fixed_deposits_frame = fixed_deposits_frame.rename(columns = {'FIXEDDEPOSITID' : 'Fixed Deposit', 'RETURNS' : 'CAGR'})
    fixed_top = fixed_deposits_frame.take([i for i in range(3)])
    mutual = mutual_funds_sol2.dropna()
    mutual['FUNDNAME.1'] = mutual['FUNDNAME'].values + ' ' + mutual['FUNDTYPE'].values
    mutual = mutual.drop(['FUNDNAME', 'FUNDTYPE'], axis = 1)
    mutual = mutual.rename(columns = {'FUNDNAME.1' : 'FUNDNAME'})
    mutual = mutual.drop(['INVESTMENTACCOUNTID', 'MUTUALFUNDID'], axis = 1)
    mutual = mutual.sort_values(by = 'RETURNS', ascending = False).reset_index(drop = True)
    mutual = mutual.rename(columns = {'FUNDNAME' : 'Fund Name', 'RETURNS' : 'CAGR'})
    mutual_top = mutual.take([i for i in range(3)])
    mutual_top = mutual_top[['Fund Name', 'CAGR']]
    stock = stocks_sol2.dropna()
    stock = stock.drop(['INVESTMENTACCOUNTID', 'STOCKID'], axis = 1)
    stock = stock.sort_values(by = 'RETURNS', ascending = False).reset_index(drop = True)
    stock = stock.rename(columns = {'STOCKNAME' : 'Stock Name', 'RETURNS' : 'CAGR'})
    stock_top = stock.take([i for i in range(3)])
    return fixed_top, mutual_top, stock_top

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
                                    *['MUTUALFUNDID', 'FUNDNAME', 'FUNDTYPE', 'INVESTMENTACCOUNTID', 'RETURNS'])
    stocks1 = merge_dataframe(stocks, stock_investment, 'INVESTMENTACCOUNTID',
                              *['STOCKID', 'STOCKNAME', 'INVESTMENTACCOUNTID', 'RETURNS'])
    final_dataframe = fixed_deposits_manipulation(fixed_deposits1)
    final_dataframe1 = mutual_fund_manipulations(mutual_funds1)
    final_dataframe2 = stock_manipulations(stocks1)
    fixed_deposits_sol2 = merge_dataframe(fixed_investment, fixed_deposits, 'INVESTMENTACCOUNTID',
                                      *['FIXEDDEPOSITID', 'INVESTMENTACCOUNTID', 'RETURNS'])
    mutual_funds_sol2 = merge_dataframe(fund_investment, mutual_funds, 'INVESTMENTACCOUNTID',
                                    *['MUTUALFUNDID', 'FUNDNAME', 'FUNDTYPE', 'INVESTMENTACCOUNTID', 'RETURNS'])
    stocks_sol2 = merge_dataframe(stock_investment, stocks, 'INVESTMENTACCOUNTID',
                              *['STOCKID', 'STOCKNAME', 'INVESTMENTACCOUNTID', 'RETURNS'])
    fixed_top, mutual_top, stock_top = manipulations_sol2(fixed_deposits_sol2, mutual_funds_sol2, stocks_sol2)
    return final_dataframe, final_dataframe1, final_dataframe2, fixed_top, mutual_top, stock_top

if __name__ == '__main__':
    final_dataframe, final_dataframe1, final_dataframe2, fixed, mutual, stock= main()
    print("Solution 1 for both user and bank to be present in 3 columns in the form of sliders:")
    solution1 = pd.concat([final_dataframe, final_dataframe1, final_dataframe2], axis = 1)
    print(solution1)
    print("Solution 2 top 3 performining investment to be shown for both user and bank in the form of 3 cards, 3 rows segmenting each type:")
    solution2 = pd.concat([fixed, mutual, stock], axis = 1)
    print(solution2)

