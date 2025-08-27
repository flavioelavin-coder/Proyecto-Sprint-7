import pandas as pd
import plotly.express as px
import streamlit as st
import numpy as np

st.title("Datos de anuncios de coches")
     

    
car_data = pd.read_csv('vehicles_us.csv') 
hist_button = st.button('Construir histograma') 
     
if hist_button: 
         st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
         fig = px.histogram(car_data, x="odometer")
         st.plotly_chart(fig, use_container_width=True)

     
st.subheader("📊 Datos generados")
st.dataframe(car_data.head())

car_data = pd.read_csv('vehicles_us.csv') 
fig = px.scatter(car_data, x="odometer", y="price") 
fig.show() 

car_data = pd.read_csv('vehicles_us.csv') 
fig = px.scatter(car_data, x="odometer", y="price") 
fig.show() 

fig = px.scatter(car_data, x="odometer", y="price") 
fig.show()