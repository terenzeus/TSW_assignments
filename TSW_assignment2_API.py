#!/usr/bin/env python
# coding: utf-8

# Get all companies' stock data for a particular day (Input to API would be date)
# 

# In[2]:


from fastapi import FastAPI

app = FastAPI()

@app.get("/api/stock-data/{date}")
def get_stock_data(date: str):
    # Retrieve all companies' stock data for the given date
    stock_data = retrieve_stock_data(date)
    return stock_data


# Get all stock data for a particular company for a particular day (Input to API would be company ID/name and date)
# 

# In[3]:


from fastapi import FastAPI

app = FastAPI()

@app.get("/api/stock-data/{company_id}/{date}")
def get_stock_data_for_company(company_id: str, date: str):
    # Retrieve the stock data for the given company and date
    stock_data = retrieve_stock_data_for_company(company_id, date)
    return stock_data


# Get all stock data for a particular company (Input to API would be company ID/name)

# In[4]:


from fastapi import FastAPI

app = FastAPI()

@app.get("/api/stock-data/{company_id}")
def get_stock_data_for_company(company_id: str):
    # Retrieve all stock data for the given company
    stock_data = retrieve_stock_data_for_company(company_id)
    return stock_data


# POST/Patch API to update stock data for a company by date

# In[5]:


from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.put("/api/stock-data/{company_id}/{date}")
@app.patch("/api/stock-data/{company_id}/{date}")
def update_stock_data_for_company(company_id: str, date: str, data: dict):
    # Update the stock data for the given company and date
    update_stock_data(company_id, date, data)
    return 'Stock data updated successfully'


# In[6]:


import pandas as pd
import pandas_datareader as pdr

def retrieve_stock_data(date):
    """Retrieve all companies' stock data for the given date"""
    # Use pandas_datareader to retrieve the stock data for all companies for the given date
    stock_data = pdr.get_data_yahoo(date)
    # Return the stock data as a dictionary
    return stock_data.to_dict()

def retrieve_stock_data_for_company(company_id, date):
    """Retrieve the stock data for the given company and date"""
    # Use pandas_datareader to retrieve the stock data for the given company and date
    stock_data = pdr.get_data_yahoo(company_id, date)
    # Return the stock data as a dictionary
    return stock_data.to_dict()

def update_stock_data(company_id, date, data):
    """Update the stock data for the given company and date"""
    # Convert the data dictionary to a pandas DataFrame
    df = pd.DataFrame.from_dict(data)
    # Update the stock data for the given company and date
    df.to_sql(name=f'stock_data_{company_id}_{date}', con=some_database_connection, if_exists='replace')


# In[ ]:




