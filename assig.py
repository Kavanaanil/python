import pandas as pd
import csv
import matplotlib.pyplot as plt
import streamlit as st


drop=st.selectbox("What type of plot to choose?",options=("ScatterPlot","BarPlot","BoxPlot","LinePlot","HistPlot"),index=0,help="Choose a plot option in dropdown")
st.write("You chose", drop,"Chart")
st.write("Here is my first attempt to use streamlit")
st.title("Sample Plots Example")

df1=pd.read_csv("Fish.csv")
df1
if drop=="ScatterPlot":
    
    
    x=list(df1.iloc[:,1])
    y=list(df1.iloc[:,6])
    plt.scatter(x,y)
    plt.xlabel('Weight')
    plt.ylabel('Width')
    plt.title('Weight to Width of species')
    ScatterPlot=plt.show()
    
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.pyplot(ScatterPlot)
    
elif drop=="BarPlot":

    x=list(df1.iloc[:,0])
    y=list(df1.iloc[:,1])
    plt.bar(x,y)
    plt.xlabel('Species')
    plt.ylabel('Weight')
    plt.title('Weight of each Species')
    
    BarPlot=plt.show()

    st.pyplot(BarPlot)
elif drop=="BoxPlot":

    x=list(df1.iloc[:,1])
    plt.xlabel('Weight of All Species')
    plt.title('Summary of Weight')

    plt.boxplot(x)
    BoxPlot=plt.show()
    st.pyplot(BoxPlot)
elif drop=="LinePlot":
    x=list(df1.iloc[:,0])
    y=list(df1.iloc[:,5])

    plt.plot(x,y)
    plt.xlabel('Species')
    plt.ylabel('Height of Species')
    plt.title('Height of each species')
    LinePlot=plt.show()
    st.pyplot(LinePlot)
elif drop=="HistPlot":

    x=list(df1.loc[:,'Species'])

    plt.hist(x,color='red')
    plt.xlabel('Species')
    plt.ylabel('Count')
    plt.title('Count of each Fish')
    HistPlot=plt.show()
    st.pyplot(HistPlot)
