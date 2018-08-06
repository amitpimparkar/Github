
# coding: utf-8

# In[2]:


#Python Code to Connect to SQL and Extract the data in CSV File

#General
import sqlite3 as sq
import pandas as pd
#To extract Data from Oracle DB
import cx_Oracle

#Defining the connection to my local DB
connection = cx_Oracle.connect('OAC_DEV/Admin123@localhost:1521/orcl.in.oracle.com')

#Creating a function to read sql by connection to the DB
def oracle_to_df(query):
    x=pd.read_sql(query,connection)
    return x

query='select * from DIPC.WC_SALES_F'#Sample Object in my DB

z=oracle_to_df(query).head()

print(z)

z.to_csv('Sample_Output.csv')#TO export output in a CSV file.

