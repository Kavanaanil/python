import pandas as pd
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_csv('toy_dataset.csv')
X = list(df.iloc[:,3])
Y = list(df.iloc[:,4])
plt.bar(X, Y, color='black',width=0.25)
plt.title("Age vs Income")
plt.xlabel("Age")
plt.ylabel("Income")
x=plt.show()
st.title("Sample deployment of graph")
st.set_option('deprecation.showPyplotGlobalUse', False)
st.pyplot(x)
