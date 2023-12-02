# dashboard.py
import streamlit as st
import markdown as md
from utilities.CustomerAnalysis import CustomerAnalysis
import pandas as pd
from css import css
from dataframe_visualisation import dataframe_visualisation
import user_dashboard


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
            user_dashboard.display_user_dashboard(usercalled)
        except:
            st.write("Issue with Input")

if sidebar_main == 'Business Visualisation' : 

    st.title('GrowthGenie App')

    st.markdown("""
        ##### wealth management dashboard for XYZ Bank
    """)
    
    bank_pin = st.text_input(label = "Bank Pin:", max_chars = 4) # default pin is 6738
    if bank_pin == '6738':
        if st.button("Details"):
            try:
                final_dataframe, final_dataframe1, final_dataframe2, fixed, mutual, stock, new_data, cust_returns, tax_liability = dataframe_visualisation()
                bankcalled =  int(bank_pin)
        #       user = CustomerAnalysis(usercalled)
                st.title("Products And Customers View")
                st.subheader('Popular And Top Performing Investments: ')
                col1, col2, col3 = st.columns(3)
                def solution_1(data):
                    lst = data.columns
                    data = pd.DataFrame(data[lst[0]])
                    data[lst[0]] = data[lst[0]].astype(str)
                    data['S#'] = data.index + 1
                    data = data.set_index('S#')
                    styled_df = data.style.applymap(lambda x: 'color: green').set_table_styles([
        {'selector': 'td', 'props': [('text-align', 'left')]},
  ])
                    return styled_df
                def create_clickable_id(id):
                    url_template= '''<a href="../../link/to/{id}" target="_blank">{id}</a>'''.format(id=id)
                    return url_template      
                new_data1 = new_data.copy()
                new_data1['NAME'] = new_data['FIRSTNAME'].values + ' ' + new_data['LASTNAME'].values    
                new_data1 = new_data1.drop(['FIRSTNAME', 'LASTNAME'], axis = 1)
                new_data1 = new_data1[['CUSTOMERID', 'NAME', 'ADDRESS', 'EMAIL', 'PHONE',
       'STOCKNAME', 'FUNDNAME', 'FIXEDDEPOSIT', 'LOANTYPE', 'NETWORTH']]
                new_data1 = new_data1.rename(columns = {'NETWORTH' : 'NETWORTH (INR)'})
                new_data1['EMAIL'] = new_data1['EMAIL'].apply(create_clickable_id)
                head = new_data1.head(10)
                csv_data = new_data1.to_csv(index = False).encode('utf-8')
                head1 = cust_returns.head(5)
                head1 = head1.rename(columns = {'1 Month Return' : '1 Month Returns (%)',
                                              '6 Month Returns' : '6 Month Returns (%)',
                                              'CAGR'  : 'CAGR (%)'})
                head1['1 Month Returns (%)'] = head1['1 Month Returns (%)'].round(2)
                head1['6 Month Returns (%)'] = head1['6 Month Returns (%)'].round(2)          
                head1['EMAIL'] = head1['EMAIL'].apply(create_clickable_id)
                st.subheader('Top 5 Returns By Customers')
                st.markdown(head1.to_html(index=False, escape=False, 
                                          render_links = True), unsafe_allow_html=True)
                st.subheader('High Net Worth Customers')
                st.download_button('Generate Comprehensive List Of High Net Worth Customers',
                                   data = csv_data, file_name = 'PersonalFinance.csv', 
                                   mime = 'text/csv', key='my_button')                
                st.markdown(head.to_html(index=False, escape=False), unsafe_allow_html=True)
                with col1:
                        # Streamlit app
                    st.subheader('Fixed Deposits')
                    # Display the styled DataFrame
                    styled_df = solution_1(final_dataframe)
                    st.dataframe(styled_df, width = 300, height = 500)
                with col2:
                    st.subheader('Mutual Funds')
                    styled_df1 = solution_1(final_dataframe1)
                    st.dataframe(styled_df1, width = 1000, height = 500)
                with col3:
                    st.subheader('Stocks')
                    final_dataframe2_ = final_dataframe2.drop_duplicates(subset = ['Stock Name'])
                    styled_df2 = solution_1(final_dataframe2_)
                    st.dataframe(styled_df2, width = 1000, height = 500)
                stock['CAGR'] = stock['CAGR'] / 100
                mutual['CAGR'] = mutual['CAGR'] / 100
                fixed['CAGR'] = fixed['CAGR'] / 100
                fixed['Fixed Deposit'] = fixed['Fixed Deposit'].astype(int).astype(str)
                with col1:
                    for _, row in fixed.iterrows():
                        investment_name = row['Fixed Deposit']
                        investment_return = row['CAGR']
                        
                        # Determine arrow color based on return
                        arrow_color = 'green' if investment_return > 0 else 'red'
                        
                        # Create HTML for the card
                        card_html = f"""
                            <div style="background-color: lightgray; padding: 10px; border-radius: 5px;">
                                <h3>Fixed Deposit: {investment_name}</h3>
                                <p>CAGR: {investment_return:.2%}</p>
                                <p style="color: {arrow_color}; font-size: 24px;">&#8593;</p>
                            </div>
                        """
                        
                        # Display the card using st.markdown
                        st.markdown(card_html, unsafe_allow_html=True)
                with col2:
                     for _, row in mutual.iterrows():
                        investment_name = row['Fund Name']
                        investment_return = row['CAGR']
                        
                        # Determine arrow color based on return
                        arrow_color = 'green' if investment_return > 0 else 'red'
                        
                        # Create HTML for the card
                        card_html1 = f"""
                            <div style="background-color: lightgray; padding: 10px; border-radius: 5px;">
                                <h3>Fund Name: {investment_name}</h3>
                                <p>CAGR: {investment_return:.2%}</p>
                                <p style="color: {arrow_color}; font-size: 24px;">&#8593;</p>
                            </div>
                        """
                        
                        # Display the card using st.markdown
                        st.markdown(card_html1, unsafe_allow_html=True)    
                with col3:
                     for _, row in stock.iterrows():
                        investment_name = row['Stock Name']
                        investment_return = row['CAGR']
                        
                        # Determine arrow color based on return
                        arrow_color = 'green' if investment_return > 0 else 'red'
                        
                        # Create HTML for the card
                        card_html2 = f"""
                            <div style="background-color: lightgray; padding: 10px; border-radius: 5px;">
                                <h3>Stock Name: {investment_name}</h3>
                                <p>CAGR: {investment_return:.2%}</p>
                                <p style="color: {arrow_color}; font-size: 24px;">&#8593;</p>
                            </div>
                        """
                        
                        # Display the card using st.markdown
                        st.markdown(card_html2, unsafe_allow_html=True) 
                with col1:
                    pass
            except Exception as a:
                st.write(a)
    elif bank_pin == '':
        st.write('Enter Bank Pin!')
    else:
        st.write('Invalid Pin!')
