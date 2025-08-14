
import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv('data/processed/merged_data.csv')

st.title('Health Research Dashboard')

year = st.slider('Select year', 2018, 2023, 2023)
df_year = df[df['year']==year]

st.subheader('Blood Pressure Distribution')
fig = px.histogram(df_year, x='systolic_bp', nbins=30, title='Systolic BP')
st.plotly_chart(fig)

st.subheader('Smoker Percentage')
smoker_pct = (df_year['smoker'].sum()/len(df_year))*100
st.metric(label='Smoker %', value=f'{smoker_pct:.2f}%')
