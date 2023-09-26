#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st


# In[2]:

st.write("Data looks like")
df=pd.read_csv("Real_estate.csv")
df


# In[11]:


x=df['number_of_convenience_stores']
y=df['distance_to_the_nearest_MRT_station']
st.write('Count of stores Vs Distance to the station')
fig = plt.figure(figsize = (30, 15))
plt.xlabel('Count of stores')
plt.ylabel('distance to the station')
plt.bar(x,y,color='red')
x=plt.show()
st.set_option('deprecation.showPyplotGlobalUse', False)
st.pyplot(x)

#URL: https://python-85ewtsul73f9hcwtrewmah.streamlit.app/
# In[ ]:




