#!/usr/bin/env python
# coding: utf-8

# In[9]:


import pandas as pd
from pandas_datareader import data

companies = ["AAPL", "GOOGl", "MSFT", "IBM", "FB"]

for company in companies:
    finance_data = data.DataReader(company, start="2010-01-01", end="2022-12-31", data_source="yahoo")
    finance_data.to_csv(company + ".csv")
    #file_path = 'C:/Users/User/Desktop/Work/Financial_data'
    #finance_data.to_csv(file_path, index=False)


# In[10]:


print(finance_data.head())


# **To configure the file**

# In[1]:


import configparser

config = configparser.ConfigParser()
config.read("config.ini")
Companies = config["companies"].values()


# **Loading the data to the table**

# In[16]:


import csv
import sqlite3

companies = ["AAPL","GOOGL","MSFT","IBM","FB"]

# Open the database connection
conn = sqlite3.connect("finance_data.db")
cursor = conn.cursor()

# Create the table
cursor.execute("""
    CREATE TABLE finance_data (
        date text,
        open real,
        high real,
        low real,
        close real,
        volume integer,
        company text
    )
""")

# Read the data from each CSV file and insert it into the database
for company in companies:
    with open(company + ".csv") as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        for row in reader:
            date = row[0]
            open = row[1]
            high = row[2]
            low = row[3]
            close = row[4]
            volume = row[5]
            cursor.execute("""
                INSERT INTO finance_data (date, open, high, low, close, volume, company)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (date, open, high, low, close, volume, company))

# Save the changes to the database
conn.commit()


# In[ ]:


# Read the data from each CSV file and insert or update it in the database
for company in companies:
    with open(company + ".csv") as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        for row in reader:
            date = row[0]
            open = row[1]
            high = row[2]
            low = row[3]
            close = row[4]
            volume = row[5]
            cursor.execute("""
                INSERT OR REPLACE INTO finance_data (date, open, high, low, close, volume, company)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (date, open, high, low, close, volume, company))

# Save the changes to the database
conn.commit()

