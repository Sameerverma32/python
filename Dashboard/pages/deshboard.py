import streamlit as st
import seaborn as sns
import plotly.express as px
import pandas as pd

df = sns.load_dataset('titanic')

st.title('Titanic deshboard') 
st.markdown("This is a simple dashboard for Titanic dataset where you can explore the dataset and visualize it ")
st.dataframe(df) # Display the dataset

st.sidebar.header("Filter options")

#gender filter
gender = st.sidebar.multiselect('Gender',
                                options=df['sex'].unique(),
                                default=df['sex'].unique())

#class filter
pclass=st.sidebar._multiselect('class',
                               options=sorted(df["class"].unique()),
                               default=sorted(df['class'].unique()))

#age filter
min_age, max_age = st.sidebar.slider('age',
                                     min_value = int(df['age'].min()),
                                     max_value = int(df['age'].max()),
                                     value = (int(df['age'].min()), int(df['age'].max())))

#create a pie chart for gender distribution
st.subheader("Gender Distribution")
fig = px.pie(df, names = 'age', title="Gender Distribution")
st.plotly_chart(fig)

#create a histogram for age distrinution
fig = px.histogram(df, x='age', title="Age Distribution", nbins=20)
st.plotly_chart(fig)

#create a bar plot for survival rate by class
fig = px.scatter(df, x='class', y='survived', title="Survival rate by Class")
st.plotly_chart(fig)

#bar plot
fig = px.line(df, x='age', y='fare', title="Age & Fare")
st.plotly_chart(fig)