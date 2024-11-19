import streamlit as st
import pandas as pd

import datetime

st.subheader("filtrar datos y capturar datos")
st.write("el procesamiento de datos a traves ciencia de datos usando Streamlit de python")

c1, c2, c3 = st.columns((3))

with c1: 
    par_nombrePais = st.text_input("Pais: ", placeholder="escriba el nombre del pais")

with c2: 
    par_Fertilidad = st.number_input("Minimo numero de hijos: ", min_value= 0, )

with c3:
    par_rangoExpectativaVida= st.slider("Rango espectativa de vida:" , min_value = 10, max_value= 100, value= (10,100))

dfDatos = pd.read_csv("http://raw.githubusercontent.com/gcastano/datasets/main/gapminder_data.csv")

if par_nombrePais != "":
    dfDatos = dfDatos [dfDatos["country"].str.upper().str.contains(par_nombrePais.upper())]

if par_Fertilidad>0:
    dfDatos = dfDatos[dfDatos["fertility"]>=par_Fertilidad]

dfDatos = dfDatos[dfDatos["lifeExpectancy"]>=par_rangoExpectativaVida[0] & (dfDatos["lifeExpectancy"]<=par_rangoExpectativaVida[1])]

st.metric("***Registros totales***", len(dfDatos))
st.dataframe(dfDatos, use_container_width=True)