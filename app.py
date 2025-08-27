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

fig = px.scatter(car_data, x="odometer", y="price") 
fig.show()

data = {
    "manufacturer": ["ford", "ford", "toyota", "toyota", "bmw", "bmw", "honda", "honda"],
    "type": ["suv", "truck", "sedan", "suv", "sedan", "coupe", "suv", "van"],
    "count": [100, 80, 120, 200, 90, 50, 160, 70]
}
df = pd.DataFrame(data)

st.title("Vehicle types by manufacturer")


fig = px.histogram(
    df,
    x="manufacturer",
    y="count",
    color="type",
    barmode="stack",   
    title="Vehicle types by manufacturer"
)

st.plotly_chart(fig)