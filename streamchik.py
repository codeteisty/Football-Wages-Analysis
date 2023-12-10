import streamlit as st
import pandas as pd
import seaborn as sns
import plotly.express as px
from links import *

df = pd.read_csv('pythonProject3/SalaryPrediction2.csv')

with st.sidebar:
    radio = st.radio(
        "Have you already predicted your football salary?",
        ("Not yet", "Yeap", "Men don't talk about their wage")
    )


st.header('Overview')
st.text('At first, I decided to visualise the number of players of each age in \nthe top 6 leagues.')
st.image(pnts[0], use_column_width=True)
st.text('Players from 22 years old to 25 prevail.')
st.text('Then I checked which nations dominate in each of the leagues.')
st.image(pnts[1], use_column_width=True)
st.image(pnts[2], use_column_width=True)
st.image(pnts[3], use_column_width=True)
button = st.button("More")
if button:
    st.image(pnts[4], use_column_width=True)
    st.image(pnts[5], use_column_width=True)
    st.image(pnts[6], use_column_width=True)
    button2 = st.button('Less')
    if button2:
        exit()

st.text("""It can be seen that national players prevail in all 6 leagues 
and there is no nation that has a big share in one of the leagues 
except from brazil players in Primera Liga (Portugal).""")
st.text('After that, I decided to make a scatter plot of wages of players of each age.')
px.scatter(df, x='Age', y='Wage')

graph = px.scatter(df, x='Age', y='Wage')
st.plotly_chart(graph, use_container_width=False, sharing="streamlit", theme="streamlit")
st.text("The only conclusion that can be made from that graph is that the youngest\nand oldest players don't have salaries higher than 3 million.")
st.text('Next, I made a boxplot of wages of players of each age.')
sns.set(rc={"figure.figsize":(18, 10)})
graph = sns.boxplot(data=df, x='Age', y='Wage', width=0.8, palette='muted').set_title('Wages of players of each age.', fontdict={'size': 30})
st.pyplot(graph.get_figure())
st.text("""Surprisingly, mean wage of players that are 31, 35, 38, and 40 years old is higher
than any other. Including the fact that a lot of players end their career at the 
age of 30 I made a conclusion that football managers and teams are ready to pay 
decent salaries to experienced players that are still physically capable of 
playing the game (otherwise they would have ended their career earlier due to 
health problems and wouldn't have been included into this dataset).""")
button = st.button("Easter egg")
if button:
    st.text('Sometimes this happens when you download streamlit:')
    st.image(pnts[7], use_column_width=True)


st.text('Made by Nikitony Podlednev')