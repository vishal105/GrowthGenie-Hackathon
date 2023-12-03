# Personal Finance : 

## 🌟 Featured on Streamlit community forum 🌟
![coverage](https://img.shields.io/badge/coverage-100%25-green) 
![version](https://img.shields.io/badge/version-0.4.1-blue)
<!-- everything tested  -->

Clairvoyant, an EXL company, is a global technology consulting and services leader that helps organizations in their business transformation by maximizing the value of data through actionable insights. Founded in 2012, Clairvoyant is headquartered in Phoenix, AZ, with offices in the US, Canada, and India and serves marquee clients in the financial services, retail, healthcare, and tech industries.
<p align = 'center' >
    <img alt = 'home_image' src = 'results/result.gif'>
</p>

## High Level Design :
* Data Source: The data source is shown as a computer. This can be any device or system that generates data, such as a web server, a database, or an IoT device.
* Data Ingestion: Data is ingested into Azure Data Lake Storage Gen2 using the HTTP Connector. This connector can be used to ingest data from a variety of sources, including web APIs, databases, and files.
* Data Transformation: Once data is in Azure Data Lake Storage Gen2, it can be transformed using various tools and services. The diagram shows Azure Data Factory being used for transformation. Azure Data Factory is a serverless data integration and ETL/ELT service that can be used to orchestrate and automate data movement and transformation.
* Data Storage: After transformation, the data is stored in Azure Data Lake Storage Gen2. This is a scalable and secure storage system that can store petabytes of data.
* Data Analysis: Data can be analyzed using a variety of tools and services. The diagram shows Azure SQL Database and Streamlit being used for analysis. Azure * * SQL Database is a relational database service that can be used to run SQL queries on the data. Streamlit is a Python library that can be used to create interactive data dashboards and applications.
* Data Publication: Data can be published to other systems and services. The diagram shows Azure Data Lake Storage Gen2 being used to publish data to Azure Blob * Storage and ML Models. Azure Blob Storage is another object storage service that can be used to store data. ML Models can be used to train and deploy machine learning models on the data.
* Azure Data Lake can be used to store, transform, and analyze data from a variety of sources. This can be used to power a variety of applications, such as data analytics, machine learning, and artificial intelligence.

Here are some additional details that are not shown in the diagram:
* The data can be structured, semi-structured, or unstructured.
* The data can be in real-time or batch-oriented.
* The data can be accessed from anywhere in the world.
* The data is secure and can be protected with access control and encryption.

## Approach : 

* So Initially I have used an <code>.ipynb</code> file to do the preprocessing and do some visualization

* Then I have made another Utilities Folder which contain <code>BusinessAnalysis.py</code> <code>CustomerAnalysis.py</code> to implement all the functions related to preprocessing and plotting

* I have imported the same file in <code>app.py</code> and used it along with streamlit to build the app.

------------------------------

## Features : 

* Shows multiple analytical charts to help me better understand the details.
* Connected to the database and automated. 
* Answers few predefined quick QNA type questions. 
* Responsive layout, can be opened in any device. 
------------------------------

## How to run? 

> To run the app you need to download this repository along with the required libraries and it the command line you have to write <code>streamlit run app.py</code> to run. 
------------------------------- 

## Document Structure 

```
Personal Finance 
│
|---- __pycache__
|
|---- .streamlit
|   |---- config.toml
|
|---- dataset 
|   xlsx files
|
|---- utilities
|   |---- __pycache__
|   |---- BusinessAnalysis.py
|   |---- CustomerAnalysis.py
|   |---- AzureSqlLoader.py
|   |---- testclass.ipynb
|   
|
|
|---- app.py
|---- auth.py
|---- user_dashboard.py
|---- dataframe_visualisation.py
|---- markdown.py
|---- Procfile 
|---- README.md
|---- requirements.txt
|---- setup.sh

```
---------------------
<p align="left">
    <img src="https://img.shields.io/badge/python%20-%2314354C.svg?&style=for-the-badge&logo=python&logoColor=white"/>
    <img src="https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white">
    <img src="https://img.shields.io/badge/numpy-%23F7931E.svg?style=for-the-badge&logo=numpy&logoColor=white">
    <img src="https://img.shields.io/badge/streamlit-%23F05033.svg?style=for-the-badge&logo=streamlit&logoColor=white">
    <img src="https://img.shields.io/badge/plotly-%037FFC.svg?style=for-the-badge&logo=plotly&logoColor=white">
    <img src="https://img.shields.io/badge/vscode-%23190458.svg?style=for-the-badge&logo=visualstudio&logoColor=white">
    <img src="https://img.shields.io/badge/Azure-0078D4?style=for-the-badge&logo=microsoft-azure&logoColor=white">
</p>

## Technologies used : 

* python library - numpy, pandas, seaborn, matplotlib, streamlit
* version control - git 
* backend - streamlit
* concept - OOP
* Cloud Technologies used- Azure Storage, Azure Data Factory, Azure SQL, Azure DataLake, Azure WebApp.

## Tools and Services : 
* IDE - Vs code 
* Application Deployment - Azure WebApp
* Code Repository - GitHub
* Dataset -Azure SQL DB, Storage Account and Data  Lake.


-----------------------
<br>

## How to Setup:

Welcome to my GrowthGenie app! To get started, follow the steps below to set up your environment variables:

### Setup Environment Variables

1. **Create a Virtual Environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate

2. **Install Dependencies::**
pip install -r requirements.txt

3. **Set Environment Variables:**
echo "export SERVER=my_server_address" >> venv/bin/activate
echo "export DATABASE=my_database_name" >> venv/bin/activate
echo "export USER=my_database_user" >> venv/bin/activate
echo "export PASSWORD=my_database_password" >> venv/bin/activate
echo "export AZURE_KEY=my_azure_key" >> venv/bin/activate

4. **Activate the Virtual Environment and run the app:**
source venv/bin/activate
streamlit run app.py

# If you Liked this project the you can consider connecting with me:
* [Akriti Kakkar](http://linkedin.com/in/akriti-k-658849178)/) 
* [Shreyans Bardia](https://www.linkedin.com/in/shreyans-bardia/)
* [Vishal Sojitra](https://www.linkedin.com/in/vishal-sojitra-dh/) 
