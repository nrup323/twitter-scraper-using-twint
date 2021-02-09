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


# In[ ]:


import numpy as np
  
#x = geek.arange(0, 10, 1) 
#print("x is:") 
#print(x) 
  
# X is an array 
c = np.savetxt(str(username) + '.txt', t, delimiter =', ')    
a = open(str(username) + '.txt', 'r')# open file in read mode 
  
print("the file contains:") 
print(a.read()) 


# In[ ]:


#vaibhaw ka kam 
hand = open('out.txt')
for line in hand:
    line = line.rstrip()
    print(line)




# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:


# importing panda library 
import pandas as pd 
  
# readinag given csv file 
# and creating dataframe 
dataframe1 = pd.read_csv("out.txt") 
  
# storing this dataframe in a csv file 
dataframe1.to_csv('out.csv',  
                  index = None) 


# In[ ]:


d = pd.read_csv('out.csv')
#d.info()
#d.head()
print(d["TEXT"])


# In[ ]:


d.head()


# In[ ]:


my_file = open("out.txt", "w")

my_file.write("First Line\n")
my_file.write("Second Line")
my_file = open("test_file.txt")
Open file for reading

content = my_file.read()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:


import twint

c = twint.Config()
c.Username = "noneprivacy"
c.Limit = 100
c.Store_csv = True
c.Output = "none.csv"
c.Lang = "en"
c.Translate = True
c.TranslateDest = "it"
twint.run.Search(c)


# In[ ]:





# In[ ]:





# In[ ]:


#url  = 'https://www.google.com/search?q='
#name = input("Give me the name")
#name = name.replace(" ", "+")
#print(name)

#print(url + name)

#r = requests.get(url)
#htmlcontent = r.content
#print(htmlcontent)
#soup  = BeautifulSoup(htmlcontent, 'html.parser')

#print(soup)

#creting the soup
#import re
#x = 'https://twitter.com/narendramodi?ref_src=twsrc%5Egoogle%7Ctwcamp%5Eserp%7Ctwgr%5Eauthor'
#atpos  = x.find('?')
#print(x.find("twitter.com"))
#print(atpos)
#stpos  = x.find('/', 10)
#print(stpos)
#username = x[stpos+1: atpos]
#username = x[20: atpos]
#print(username)
#y = re.findall('^https://twitter.com/.+?:', x)
#print(y)
#y = "none"


#title  =soup.title


#print(title.string)
#print(title)
##print(title.string)
#anchors = soup.find_all('a')
#print(anchors)
#paras = soup.find_all('p')
#print(paras)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




