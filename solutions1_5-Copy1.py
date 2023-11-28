#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import warnings

warnings.filterwarnings('ignore')


class DataLoader:
    @staticmethod
    def load_data(file_name, **kwargs):
        file_path = r'C:\Users\Akriti Kakkar\Downloads\GrowthGenie-Hackathon-main\GrowthGenie-Hackathon-main\dataset\{}.xlsx'.format(
            file_name)
        data = pd.read_excel(file_path, **kwargs)
        return data


class DataManipulation:
    @staticmethod
    def slice_data(data, account_type):
        sliced_data = data[data['ACCOUNTTYPE'] == account_type].reset_index(drop=True)
        return sliced_data

    @staticmethod
    def merge_data(df1, df2, on, *args):
        data = pd.merge(df1, df2, how='left', on=on)
        data = data[list(args)]
        return data


class FixedDepositsManipulation(DataManipulation):
    @staticmethod
    def manipulate_data(fixed_deposits1):
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


class MutualFundManipulations(DataManipulation):
    @staticmethod
    def manipulate_data(mutual_funds1):
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

    
class StockManipulations(DataManipulation):
    @staticmethod
    def manipulate_data(stocks1):
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


class SolutionTwoManipulations(DataManipulation):
    @staticmethod
    def manipulate_data(fixed_deposits_sol2, mutual_funds_sol2, stocks_sol2):
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


class SolutionThreeManipulations(DataManipulation):
    @staticmethod
    def manipulate_data(fixed_sol3, mutual_sol3, stock_sol3, loans, customers):
        data = pd.merge(fixed_sol3, mutual_sol3, how = 'outer', on = 'INVESTMENTACCOUNTID')
        data1 = pd.merge(data, stock_sol3, how = 'outer', on = 'INVESTMENTACCOUNTID')
        loan3 = loans[loans['LOANSTATUS'] == 'Approved'].reset_index(drop = True)
        loan = loan3.groupby('CUSTOMERID', as_index = False).agg({'LOANAMOUNT' : sum})
        product = stock_sol3[['CUSTOMERID', 'STOCKNAME']]
        product1 = mutual_sol3[['CUSTOMERID', 'FUNDNAME']]
        product2 = fixed_sol3[['CUSTOMERID', 'FIXEDDEPOSITID']]
        product3 = loan3[['CUSTOMERID', 'LOANTYPE']]
        data1[['PRINCIPALAMOUNT', 'INVESTMENTAMOUNT', 'PURCHASEPRICE', 'QUANTITY']] = data1[[
        'PRINCIPALAMOUNT', 'INVESTMENTAMOUNT', 'PURCHASEPRICE', 'QUANTITY']].fillna(0)
        data1['STOCKINVESTMENT'] = data1['PURCHASEPRICE'] * data1['QUANTITY']
        data1 = data1[['CUSTOMERID', 'INVESTMENTACCOUNTID', 'PRINCIPALAMOUNT', 'INVESTMENTAMOUNT', 'STOCKINVESTMENT']]
        new_data = data1.groupby(['CUSTOMERID', 'INVESTMENTACCOUNTID'], as_index = False).agg({'PRINCIPALAMOUNT' : sum, 
                                                                                               'INVESTMENTAMOUNT' : sum,
                                                                                               'STOCKINVESTMENT' : sum})
        new_data = new_data.reset_index(drop = True)
        new_data['INVESTMENTS'] = new_data[['PRINCIPALAMOUNT' , 'INVESTMENTAMOUNT' , 'STOCKINVESTMENT']].sum(axis = 1)
        new_data['CUSTOMERID'] = new_data['CUSTOMERID'].astype(int)
        new_merge = pd.merge(loan, new_data, how = 'outer', on = 'CUSTOMERID')
        new_data1 = new_merge.drop(['INVESTMENTACCOUNTID', 'PRINCIPALAMOUNT', 'INVESTMENTAMOUNT',
                              'STOCKINVESTMENT'], axis = 1)
        new_data1[['LOANAMOUNT', 'INVESTMENTS']] = new_data1[['LOANAMOUNT', 'INVESTMENTS']].fillna(0)
        new_data1['NETWORTH'] = new_data1['INVESTMENTS'] - new_data1['LOANAMOUNT']
        new_data11 = new_data1[['CUSTOMERID', 'NETWORTH']]
        new_data11 = new_data11.sort_values(by = 'NETWORTH', ascending = False)

        productstock = product.dropna(subset=['STOCKNAME'])
        grouped_product = productstock.groupby('CUSTOMERID')['STOCKNAME'].agg(lambda x: ', '.join(x)).reset_index()

        productfund = product1.dropna(subset=['FUNDNAME'])
        grouped_product1 = productfund.groupby('CUSTOMERID')['FUNDNAME'].agg(lambda x: ', '.join(x)).reset_index()

        productfixed = product2.dropna(subset=['FIXEDDEPOSITID'])
        productfixed['FIXEDDEPOSITID'] = productfixed['FIXEDDEPOSITID'].astype(int)
        productfixed['FIXEDDEPOSITID'] = productfixed['FIXEDDEPOSITID'].astype(str)
        grouped_product2 = productfixed.groupby('CUSTOMERID')['FIXEDDEPOSITID'].agg(lambda x: ', '.join(x)).reset_index()
        grouped_product2 = grouped_product2.rename(columns = {'FIXEDDEPOSITID' : 'FIXEDDEPOSIT'})

        productloan = product3.dropna(subset=['LOANTYPE'])
        grouped_product3 = productloan.groupby('CUSTOMERID')['LOANTYPE'].agg(lambda x: ', '.join(x)).reset_index()

        merge_products = pd.merge(customers, grouped_product, on = 'CUSTOMERID', how = 'left')
        merge_products1 = pd.merge(merge_products, grouped_product1, on = 'CUSTOMERID', how = 'left')
        merge_products2 = pd.merge(merge_products1, grouped_product2, on = 'CUSTOMERID', how = 'left')
        merge_products3 = pd.merge(merge_products2, grouped_product3, on = 'CUSTOMERID', how = 'left')
        #merge_products1['FIXEDDEPOSITID'] = merge_products1['FIXEDDEPOSITID'].astype(int)
        final_cust = merge_products3[['CUSTOMERID', 'FIRSTNAME', 'LASTNAME', 'ADDRESS', 'EMAIL', 'PHONE', 'STOCKNAME', 'FUNDNAME',
                                      'FIXEDDEPOSIT', 'LOANTYPE']]

        new_data01 = new_data11.groupby('CUSTOMERID', as_index = False).agg({'NETWORTH' : sum})

        final_frame = pd.merge(final_cust, new_data01, how = 'left', on = 'CUSTOMERID')
        final_frame = final_frame.dropna(subset = ['NETWORTH'])
        final_frame = final_frame.sort_values(by = 'NETWORTH', ascending = False).reset_index(drop = True)
        return final_frame



class Returns:
    @staticmethod
    def calculate_returns(investment_accounts, customers):
        data = investment_accounts.groupby('CUSTOMERID', as_index = False).agg({'RETURNS' : sum})
        data = data.sort_values(by = 'RETURNS', ascending = False).reset_index(drop = True)
        data1 = data.copy()
        data1['6 Month Returns'] = ((1 + data['RETURNS'])**(6/12)) - 1
        data1['1 Month Return'] = ((1 + data['RETURNS'])**(1/12)) - 1
        cust_data = pd.merge(data1, customers, on = 'CUSTOMERID', how = 'left')
        cust_top = cust_data.take([i for i in range(5)])
        cust_top['Name'] = cust_top['FIRSTNAME'] + ' ' + cust_top['LASTNAME']
        cust_top = cust_top.rename(columns = {'RETURNS' : 'CAGR'})
        cust_top = cust_top[['Name', 'EMAIL', 'PHONE', '1 Month Return', '6 Month Returns', 'CAGR']]
        return cust_top


class TaxLiability:
    @staticmethod
    def calculate_tax_liability(investment_accounts):
        #call dataframe
        df = investment_accounts.copy()
        df = df.rename(columns = {'RETURNS' : 'CAGR'})
        # Add additional columns for holding period, gains, and tax liability
        df['HoldingPeriod'] = (pd.to_datetime(df['INVESTMENTENDDATE']) - pd.to_datetime(df['INVESTMENTSTARTDATE'])).dt.days / 365
        df['Gains'] = df['INVESTMENTPORTFOLIO'] * (df['CAGR'] / 100)

        # Calculate tax liability based on investment type and holding period
        df['TaxLiability'] = 0  # Initialize tax liability column

        # Calculate tax liability for Mutual Funds
        mutual_funds_mask = df['ACCOUNTTYPE'] == 'Mutual Funds'
        df.loc[mutual_funds_mask, 'TaxLiability'] = (
            df.loc[mutual_funds_mask, 'Gains'] * 0.15  # Tax rate for holding period <= 1 year
            + (df.loc[mutual_funds_mask, 'Gains'] - 100000) * 0.10  # Tax rate for holding period > 1 year
        )

        # Calculate tax liability for Stocks
        stocks_mask = df['ACCOUNTTYPE'] == 'Stocks'
        df.loc[stocks_mask, 'TaxLiability'] = (
            df.loc[stocks_mask, 'Gains'] * 0.15  # Tax rate for holding period <= 1 year
            + (df.loc[stocks_mask, 'Gains'] - 100000) * 0.10  # Tax rate for holding period > 1 year
        )

        # Calculate tax liability for Fixed Deposits
        fd_mask = df['ACCOUNTTYPE'] == 'Fixed Deposits'
        df.loc[fd_mask, 'TaxLiability'] = df.loc[fd_mask, 'Gains'] * 0.10  # Tax rate for fixed deposits

        # Sum up tax liabilities for each customer
        total_tax_liabilities = df.groupby('CUSTOMERID').agg({'TaxLiability' : sum, 'Gains' : sum})

        # Display the resulting DataFrame with tax liabilities
        total_tax_liabilities = total_tax_liabilities.rename(columns = {'TaxLiability' : 'Tax Liability'})
        return total_tax_liabilities


class MainApplication:
    @staticmethod
    def run():
        accounts = DataLoader.load_data('accounts', parse_dates=['OPENINGDATE', 'LASTTRANSACTIONDATE'])
        customers = DataLoader.load_data('customers')
        fixed_deposits = DataLoader.load_data('fixed_deposits', parse_dates=['MATURITYDATE'])
        mutual_funds = DataLoader.load_data('mutual_funds', parse_dates=['INVESTMENTDATE'])
        stocks = DataLoader.load_data('stocks')
        investment_accounts = DataLoader.load_data('investment_accounts',
                                                   parse_dates=['INVESTMENTSTARTDATE', 'INVESTMENTENDDATE'])
        loans = DataLoader.load_data('loans', parse_dates=['DISBURSEMENTDATE'])

        # Instantiate classes
        fixed_class = FixedDepositsManipulation()
        mutual_class = MutualFundManipulations()
        stock_class = StockManipulations()
        solution_two_class = SolutionTwoManipulations()
        solution_three_class = SolutionThreeManipulations()
        returns_class = Returns()
        tax_liability_class = TaxLiability()

        # Perform data manipulations
        fixed_deposits1 = DataManipulation.merge_data(fixed_deposits, fixed_class.slice_data(investment_accounts, 'Fixed Deposits'),
                                                      'INVESTMENTACCOUNTID', *['FIXEDDEPOSITID', 'INVESTMENTACCOUNTID', 'INTERESTRATE'])
        mutual_funds1 = DataManipulation.merge_data(mutual_funds, mutual_class.slice_data(investment_accounts, 'Mutual Funds'),
                                                    'INVESTMENTACCOUNTID', *['MUTUALFUNDID', 'FUNDNAME', 'FUNDTYPE', 'INVESTMENTACCOUNTID', 'RETURNS'])
        stocks1 = DataManipulation.merge_data(stocks, stock_class.slice_data(investment_accounts, 'Stocks'),
                                              'INVESTMENTACCOUNTID', *['STOCKID', 'STOCKNAME', 'INVESTMENTACCOUNTID', 'RETURNS'])

        # Call manipulation methods
        final_dataframe = fixed_class.manipulate_data(fixed_deposits1)
        final_dataframe1 = mutual_class.manipulate_data(mutual_funds1)
        final_dataframe2 = stock_class.manipulate_data(stocks1)
        fixed_deposits_sol2 = DataManipulation.merge_data(fixed_class.slice_data(investment_accounts, 'Fixed Deposits'),
                                                          fixed_deposits, 'INVESTMENTACCOUNTID',
                                                          *['FIXEDDEPOSITID', 'INVESTMENTACCOUNTID', 'RETURNS'])
        mutual_funds_sol2 = DataManipulation.merge_data(mutual_class.slice_data(investment_accounts, 'Mutual Funds'),
                                                        mutual_funds, 'INVESTMENTACCOUNTID',
                                                        *['MUTUALFUNDID', 'FUNDNAME', 'FUNDTYPE', 'INVESTMENTACCOUNTID', 'RETURNS'])
        stocks_sol2 = DataManipulation.merge_data(stock_class.slice_data(investment_accounts, 'Stocks'),
                                                  stocks, 'INVESTMENTACCOUNTID',
                                                  *['STOCKID', 'STOCKNAME', 'INVESTMENTACCOUNTID', 'RETURNS'])
        fixed_top, mutual_top, stock_top = solution_two_class.manipulate_data(fixed_deposits_sol2, mutual_funds_sol2, stocks_sol2)
        fixed_sol3 = DataManipulation.merge_data(fixed_class.slice_data(investment_accounts, 'Fixed Deposits'),
                                                 fixed_deposits, 'INVESTMENTACCOUNTID',
                                                 *['CUSTOMERID', 'FIXEDDEPOSITID', 'INVESTMENTACCOUNTID', 'PRINCIPALAMOUNT'])
        mutual_sol3 = DataManipulation.merge_data(mutual_class.slice_data(investment_accounts, 'Mutual Funds'),
                                                  mutual_funds, 'INVESTMENTACCOUNTID',
                                                  *['CUSTOMERID', 'MUTUALFUNDID', 'FUNDNAME', 'FUNDTYPE', 'INVESTMENTACCOUNTID',
                                                    'INVESTMENTAMOUNT'])
        stock_sol3 = DataManipulation.merge_data(stock_class.slice_data(investment_accounts, 'Stocks'),
                                                 stocks, 'INVESTMENTACCOUNTID',
                                                 *['CUSTOMERID', 'STOCKID', 'STOCKNAME', 'INVESTMENTACCOUNTID', 'PURCHASEPRICE', 'QUANTITY'])
        new_data = solution_three_class.manipulate_data(fixed_sol3, mutual_sol3, stock_sol3, loans, customers)
        cust_returns = returns_class.calculate_returns(investment_accounts, customers)
        tax_liability1 = tax_liability_class.calculate_tax_liability(investment_accounts)

        print("Solution 1 for both user and bank to be present in 3 columns in the form of sliders:")
        solution1 = pd.concat([final_dataframe, final_dataframe1, final_dataframe2], axis=1)
        print(solution1)
        print("Solution 2 top 3 performing investment to be shown for both user and bank in the form of 3 cards, 3 rows segmenting each type:")
        solution2 = pd.concat([fixed_top, mutual_top, stock_top], axis = 1)
        print(solution2)
        print('''Solution 3 (view only for banks) top 10 customers net woth in pie chart and products in 3 seaborn charts,
              download button to download and view the entire dataframe''')
        print(new_data)
        print('''Solution 4 (view only for bank, convert this dataframe to pandas stylers and just write it on streamlit using
        st.write(cust_returns))''')
        print(cust_returns)
        print('''Solution 5 (view only for customer, link customer id with login  and show gains and tax liability as one/two
              cards on top of the dashboard)''')
        print(tax_liability1)
        return final_dataframe, final_dataframe1, final_dataframe2, fixed_top, mutual_top, stock_top, new_data, cust_returns, tax_liability1
if __name__ == "__main__":
    MainApplication.run()


# In[ ]:





# In[ ]:




