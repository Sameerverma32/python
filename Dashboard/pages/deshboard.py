import streamlit as st
import seaborn as sns
import plotly.express as px
import pandas as pd

df = sns.load_dataset('titanic')

st.title('Titanic Dashboard')
st.markdown("This is a simple dashboard for Titanic dataset where you can explore the dataset and visualize it") 

st.dataframe(df) # Display the dataset

st.sidebar.header("Filter options")

#gender filter
gender = st.sidebar.multiselect('Gender',
                                options=df['sex'].unique(),
                                default=df['sex'].unique())

#class filter
pclass = st.sidebar.multiselect('Class',
                                options = sorted(df['class'].unique()),
                                default = sorted(df['class'].unique()))

#age filter
min_age, max_age = st.sidebar.slider('Age',
                                    min_value = int(df['age'].min()),
                                    max_value = int(df['age'].max()),
                                    value = (int(df['age'].min()), int(df['age'].max())))

filtered_data = df[
    (df['sex'].isin(gender)) &
    (df['class'].isin(pclass)) &
    (df['age'] >= min_age) &
    (df['age'] <= max_age)
]

#create a pie chart for gender distribution
st.subheader("Gender Distribution")
gender_count = filtered_data['sex'].value_counts()
fig = px.pie(names=gender_count.index, values=gender_count.values,
     title="Gender Distribution")
st.plotly_chart(fig)

#create a histogramfor age distribution
fig = px.histogram(filtered_data, x='age', title="Age Distribution", nbins=20)
st.plotly_chart(fig)