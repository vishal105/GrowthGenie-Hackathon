import pandas as pd
import pyodbc
import os
from dotenv import load_dotenv


class AzureSQLLoader:
    def __init__(self, server: str = None, database: str = None, username: str = None, password: str = None, driver: str = "{ODBC Driver 17 for SQL Server}"):
        load_dotenv()
        self.server: str = server if server else os.getenv('server')
        self.database: str = database if database else os.getenv('database')
        self.username: str = username if username else os.getenv('userazure')
        self.password: str = password if password else os.getenv('password')
        self.driver: str = driver
        print(self.username)
        # Initialize connection attribute to None
        self.conn = None

        # Connect to the database
        self.connect()

    def connect(self):
        try:
            # Create a connection string
            conn_str = f'DRIVER={self.driver};SERVER={self.server};DATABASE={self.database};Uid={self.username};Pwd={self.password};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;'
            print(conn_str)

            # Establish a connection
            self.conn = pyodbc.connect(conn_str)
            print("Connected to the database.")
        except Exception as e:
            print(f"Connection error: {e}")

    def load_table(self, table_name):
        try:
            # Query to select all rows from the table
            query = f'SELECT * FROM {table_name}'

            # Use pandas to read the SQL query result into a DataFrame
            df = pd.read_sql(query, self.conn)
            print(f"Table '{table_name}' loaded into DataFrame.")
            return df
        except Exception as e:
            print(f"Error loading table: {e}")

    def load_customer(self, table_name,customer):
        try:
            # Query to select all rows from the table
            query = f'SELECT * FROM {table_name} WHERE CUSTOMERID = {customer}'

            # Use pandas to read the SQL query result into a DataFrame
            df = pd.read_sql(query, self.conn)
            print(f"Table '{table_name}' loaded into DataFrame.")
            return df
        except Exception as e:
            print(f"Error loading table: {e}")
    def load_customer_join_inv(self, table_name,customer):
        try:
            # Query to select all rows from the table
            query = f'SELECT s.*,ia.CUSTOMERID FROM {table_name} s JOIN InvestmentAccounts ia ON s.INVESTMENTACCOUNTID = ia.INVESTMENTACCOUNTID WHERE CUSTOMERID = {customer}'

            # Use pandas to read the SQL query result into a DataFrame
            df = pd.read_sql(query, self.conn)
            print(f"Table '{table_name}' loaded into DataFrame.")
            return df
        except Exception as e:
            print(f"Error loading table: {e}")

    def load_customer_join_acc(self, table_name,customer):
        try:
            # Query to select all rows from the table
            query = f'SELECT s.*,ia.CUSTOMERID FROM Transactions s JOIN Accounts ia ON s.ACCOUNTID = ia.ACCOUNTID WHERE CUSTOMERID = {customer}'

            # Use pandas to read the SQL query result into a DataFrame
            df = pd.read_sql(query, self.conn)
            print(f"Table '{table_name}' loaded into DataFrame.")
            return df
        except Exception as e:
            print(f"Error loading table: {e}")

    def close_connection(self):
        try:
            # Close the database connection
            if self.conn:
                self.conn.close()
                print("Connection closed.")
            else:
                print("No active connection to close.")
        except Exception as e:
            print(f"Error closing connection: {e}")

# Example usage



