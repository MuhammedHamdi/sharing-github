#!/usr/bin/env python
# coding: utf-8

# # Date / Time : The date and time of the Uber pickup
# # lat :  The latitude of the Uber pickup
# # lon :The longitude of the Uber pickup
# # Base : The TLC base company code affiliated with the Uber pickup

# In[1]:



get_ipython().run_line_magic('pylab', 'inline')
import pandas
import numpy
import sklearn
import seaborn
import plotly.graph_objs as go
from plotly.offline import init_notebook_mode, iplot
init_notebook_mode()


# # load csv file into momery
# 

# In[2]:


data = pandas.read_csv('Documents/uber-raw-daya-apr .csv')


# In[3]:


data


# # convert date/time and add some useful columns

# In[4]:


data['Date/Time'] = data['Date/Time'].map(pandas.to_datetime)


# In[5]:


data.tail()


# In[6]:


dt = data ['Date/Time'][0]


# In[7]:


dt.day


# In[8]:


dt = data ["Date/Time"][564486]


# In[9]:


dt.day


# In[10]:


def get_dom(dt):
    return dt.day
data['dom'] = data['Date/Time'].map(get_dom)


# In[11]:


data.tail()


# In[13]:


def get_weekday(dt):
    return dt.weekday()

data['weekday'] = data['Date/Time'].map(get_weekday)

def get_hour(dt):
    return dt.hour

data['hour'] = data['Date/Time'].map(get_hour)

data.tail()


# # analyze the DoM

# In[16]:


hist(data.dom, bins=20, rwidth=.7, range=(0.5, 30.5))
xlabel('date of the month')
ylabel('frequency')
title('Frequency by DoM - uber - Apr 2014')


# In[17]:


def count_rows(rows):
    return len(rows)

by_date = data.groupby('dom').apply(count_rows)
by_date


# In[18]:


plot(by_date)


# In[19]:


by_date_sorted = by_date.sort_values()
by_date_sorted


# In[20]:


bar(range(1, 31), by_date_sorted)
xticks(range(1,31), by_date_sorted.index)
xlabel('date of the month')
ylabel('frequency')
title('Frequency by DoM - uber - Apr 2014')
("")


# # analyze the hour
# 

# In[21]:


hist(data.weekday, bins=7, range =(-.5,6.5), rwidth=.8, color='#AA6666', alpha=.4)
xticks(range(7), 'Mon Tue Wed Thu Fri Sat Sun'.split())


# # cross analysis (hour, dow)
# 

# In[22]:


data.groupby('hour weekday'.split()).apply(count_rows)


# In[23]:


data.groupby('weekday hour'.split()).apply(count_rows).unstack()


# In[24]:


by_cross = data.groupby('weekday hour'.split()).apply(count_rows).unstack()


# In[25]:


seaborn.heatmap(by_cross)


# In[26]:


hist(data['Lat'], bins=100, range = (40.5, 41))
("")


# In[27]:


hist(data['Lon'], bins=100, range = (-74.1, -73.9));


# In[28]:


hist(data['Lon'], bins=100, range = (-74.1, -73.9), color='g', alpha=.5, label = 'longitude')
grid()
legend(loc='upper left')
twiny()
hist(data['Lat'], bins=100, range = (40.5, 41), color='r', alpha=.5, label = 'latitude')
legend(loc='best')
("")


# In[ ]:




