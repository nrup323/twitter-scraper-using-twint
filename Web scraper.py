#!/usr/bin/env python
# coding: utf-8

# In[8]:


#import requests
#import html5lib
#import sys
#import webbrowser
#from bs4 import BeautifulSoup
import re
from googlesearch import search
#pip install google
import twint
#pip3 install twint
import nest_asyncio
#pip3 install nest_asyncio
nest_asyncio.apply()
print("Done")


# In[11]:


#https://www.geeksforgeeks.org/performing-google-search-using-python-code/
name = input("Give me the name")
query = "twitter" + name 
#print(query)
for j in search(query, tld="com", num=1, stop=1, pause=2): 
    print(j) 
    if(j.find("twitter.com")):
        atpos  = j.find('?')
        username = j[20: atpos]
        print(username)

        
        


# In[3]:


#https://github.com/twintproject/twint
c = twint.Config()
c.Username = username
#c.search = " "
c.Since = "2021-01-01"
c.limit = 1000
c.Store_csv = True
c.Output = str(username)+  ".csv"
twint.run.Search(c)


# In[4]:


#reading a csv file

import pandas as pd

data = pd.read_csv(str(username)+  ".csv") 
#data.describe()
data.head()


# In[5]:


twits = (data['tweet'])
#type(twits)
#print(twits)
#twits.shape
type(twits)


# In[6]:


twits.to_csv(str(username)+ "_final.csv")

#t = data['tweet'].to_numpy()
#print(t)


# In[7]:


t.shape
type(t)



