#!/usr/bin/env python
# coding: utf-8

# # Data module class 2
# Reading documentation: Pandas and BeautifulSoup

# In[1]:


import pandas as pd
from bs4 import BeautifulSoup
import requests


# In[5]:


# download and import BeautifulSoup if you need to
# !pip install beautifulsoup4
get_ipython().system('pip install beautifulsoup4')


# In[2]:


# downloading lxml
get_ipython().system('pip install lxml')


# In[ ]:





# ## Pandas
# ### Terminology reference
# #### Data structures
# ##### 1-dimensional data (create Series)
# 
# |pandas abbreviation|definition|example|
# |---|---|---|
# |dict|Python dictionary|`{'a': 'value', 'b': 'value'}`|
# |ndarray|N-dimensional array (can be 1 or 2 dimensional)|`[0, 1, 2, 3]`|
# |scalar|Single value|`100`|
# |list|Python list|`[0, 1, 2, 3]`|
# 
# ##### 2-dimensional data (create DataFrames)
# 
# |pandas term|example|
# |---|---|
# |ndarray|`[[0, 1, 2, 3], [4, 5, 6, 7]]`|
# |dict of ndarrays|`{'one': [1, 2, 3, 4], 'two': [4, 3, 2, 1]}`|
# |list of dicts|`[{'id': 1, 'info': 'text'}, {'id': 2, 'info': 'more text'}]`|

# #### How do these look when loaded in pandas?
# [Taken from the Pandas User Guide](https://pandas.pydata.org/docs/user_guide/dsintro.html)

# In[55]:


pd.Series({'a': 'value', 'b': 'value'})


# In[56]:


pd.Series([0, 1, 2, 3])


# In[57]:


pd.Series(5)


# In[80]:


pd.DataFrame([{'id': 1, 'info': 'text'}, {'id': 2, 'info': 'more text'}])


# In[81]:


pd.DataFrame([[0, 1, 2, 3], [4, 5, 6, 7]])


# #### Other terms
# [See pd.DataFrame() as an example](https://pandas.pydata.org/docs/reference/api/pandas.to_datetime.html#pandas.to_datetime)
# 
# - parameters
#     - Information that a function accepts 
# - args
#     - Arguments that are required (or things that the function needs in order to run)
#     - i.e. data for your DataFrame
# - kwargs (even though Pandas does not identify them as such)
#     - Keyword arguments: optional arguments not necessary for a function to run, but will tell the function to behave in a different way than the default. Called "keyword" arguments because you have to identify the name of the variable
#     - i.e. errors='raise'

# ### 1. Let's practice input/output with Pandas with the following links.
# Use Panda's [IO Tools](https://pandas.pydata.org/pandas-docs/stable/user_guide/io.html) section of their documentation to grab these datasets
# 
# - [Avengers Wikia data - FiveThirtyEight](https://raw.githubusercontent.com/fivethirtyeight/data/master/comic-characters/marvel-wikia-data.csv) | [Documentation here](https://github.com/fivethirtyeight/data/tree/master/avengers)
# - [List of sovereign states - Wikipedia](https://en.wikipedia.org/wiki/List_of_sovereign_states)
# - [Homeless housing - LA Times](https://raw.githubusercontent.com/kyleykim/R_Scripts/master/la-me-ln-hhh-unequal/revised_data/master_data_geocoded.csv) | [Documentation](https://github.com/kyleykim/R_Scripts/tree/master/la-me-ln-hhh-unequal)

# In[19]:


df_avengers = pd.read_csv("https://raw.githubusercontent.com/fivethirtyeight/data/master/comic-characters/marvel-wikia-data.csv")


# In[4]:


df_sovereign_states = pd.read_html('https://en.wikipedia.org/wiki/List_of_sovereign_states')


# In[20]:


df_homeless_housing = pd.read_csv("https://raw.githubusercontent.com/kyleykim/R_Scripts/master/la-me-ln-hhh-unequal/revised_data/master_data_geocoded.csv")


# ### 2. Let's practice working with missing data and selecting these values
# #### For each DataFrame, either select all the missing values of one column or select a unique categorical value.
# The [Indexing and selecting data¶](https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html) section of Pandas documentation will help

# #### a. Avengers

# In[18]:


df_avengers.info()


# In[7]:


df_avengers['ID'].unique()


# In[8]:


df_avengers[df_avengers['ID'].isna()]


# In[ ]:





# #### b. Countries

# In[11]:


df_sovereign_states[0]


# In[13]:


df_sovereign_states[0].info()


# In[16]:


df_sovereign_states[0][df_sovereign_states[0]['Common and formal names'].isna()]


# In[ ]:





# #### c. LA homeless housing

# In[22]:


df_homeless_housing.info()


# In[27]:


df_homeless_housing['status'].unique()


# In[30]:


df_homeless_housing[df_homeless_housing['status'] == 'Pending City Council approval']


# In[ ]:





# ### 3. Let's practice cleaning with intent

# #### Use each the three datasets loaded in to generate a question you want to answer with the data
# ##### Tips
# - Show the column list the column types and null values
# - Find unique values to look at categorical data

# #### a. Avengers
# ##### Question
# - How many female Avengers are alive?
# 
# ##### What cleaning do I need to do to answer the question
# - List Avengers that are female
# - Filter who are alive 
# - Count with 'len'

# In[32]:


# show the dataframe info here to get you started 
df_avengers.info()


# In[38]:


df_avengers['SEX'].value_counts()


# In[40]:


df_avengers[df_avengers['SEX'] == 'Female Characters']


# In[41]:


df_avengers['ALIVE'].value_counts()


# In[43]:


len(df_avengers[(df_avengers['SEX'] == 'Female Characters') & (df_avengers['ALIVE'] == 'Living Characters')])


# In[ ]:





# #### b. Countries
# ##### Question
# - What is the status and recognition of sovereignty in Israel?
# 
# ##### What cleaning do I need to do to answer the question
# - Find how Israel is written in the table using .unique()
# - Filter for Israel
# - Allow the text descriptions to be longer

# In[33]:


df_sovereign_states[0].info()


# In[80]:


df_sovereign_states[0]['Common and formal names'].unique()


# In[89]:


df_israel = df_sovereign_states[0][df_sovereign_states[0]['Common and formal names'] == 'Israel\xa0– State of Israel']


# In[95]:


pd.set_option("display.max_colwidth", 1000)
df_israel


# In[ ]:





# #### c. LA homeless housing
# ##### Question
# - Among the housing projects that are yet to be approved, which offers the max number of units?
# 
# ##### What cleaning do I need to do to answer the question
# - Find what are the categories in status 
# - Filter for housing projects that are not yet approved
# - Find the max

# In[34]:


df_homeless_housing.info()


# In[101]:


df_homeless_housing.status.unique()


# In[98]:


df_homeless_housing[df_homeless_housing.status == 'Pending City Council approval']


# In[103]:


df_homeless_housing[df_homeless_housing.status == 'Pending City Council approval'].max()


# Take a look at the [LA Times'](https://github.com/datadesk/notebooks) or [FiveThirtyEight's](https://github.com/fivethirtyeight/data) for more practice

# ## BeautifulSoup
# [BeautifulSoup documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)

# In[48]:


# load in the HTML and format for BS
sp500_url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'


# In[49]:


sp500 = requests.get(sp500_url)


# In[50]:


sp500_bs = BeautifulSoup(sp500.content)


# In[51]:


sp500_bs


# In[52]:


# finds the title tag
sp500_bs.title


# In[57]:


# grab the first a tag
sp500_bs.a


# In[55]:


# finds all a tags
sp500_bs.find_all("a")


# In[56]:


# find all elements with the class "mw-jump-link"
sp500_bs.find_all(class_ = "mw-jump-link")


# ### Traverse the DOM

# In[60]:


# we know the table we want is the first table in the DOM
# then we want to to read tr tags as groups of cells in a row and td tags as cells


# In[61]:


# find where the data you want resides (a tag, class name, etc)
sp500_table = sp500_bs.find_all("table")[0]


# In[63]:


# find_all tr
sp500_trs = sp500_table.find_all("tr")


# In[68]:


# separate the first tr tag row for the header
sp500_th = sp500_trs[0].find_all('th')
sp500_header = []
for th in sp500_th:
    sp500_header.append(th.text)


# In[70]:


# for each tr, find tds then for each td get text inside, then save to new array
sp500_list = []
for tr in sp500_trs[1:]:
    tds = tr.find_all('td')
    tr_list = []
    for (i, td) in enumerate(tds):
        if(i == 2):
            tr_list.append(td.find('a')['href'])
        else:
            tr_list.append(td.text)
    sp500_list.append(tr_list)


# In[73]:


sp500_df = pd.DataFrame(sp500_list, columns=sp500_header)
sp500_df


# In[ ]:





# ### We can do more cleaning here

# In[ ]:




