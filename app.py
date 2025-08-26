import pandas as pd
import plotly.express as px
import streamlit as st
import numpy as np

st.title("Datos de anuncios de coches")
     

    
     car_data = pd.read_csv('vehicles_us.csv') # leer los datos
     hist_button = st.button('Construir histograma') # crear un botón
     
     if hist_button: 
         st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
         
        
         fig = px.histogram(car_data, x="odometer")
     
         
         st.plotly_chart(fig, use_container_width=True)
     
st.subheader("📊 Datos generados")
st.dataframe(df.head())

car_data = pd.read_csv('vehicles_us.csv') # leer los datos
fig = px.scatter(car_data, x="odometer", y="price") # crear un gráfico de dispersión
fig.show() 

car_data = pd.read_csv('vehicles_us.csv') # leer los datos
fig = px.scatter(car_data, x="odometer", y="price") # crear un gráfico de dispersión
fig.show() #
