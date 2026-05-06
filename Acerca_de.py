import streamlit as st
import streamlit.components.v1 as components

# Configuración de la página
st.set_page_config(layout="wide")

st.title("Mapa interactivo – Región de Ñuble")

st.write("Mapa cargado desde servidor local (http://localhost:8000)")

# Insertar el mapa con iframe (FORMA CORRECTA)
components.iframe(
    "https://mapa-nuble.netlify.app/",
    height=800,
    width="100%"
)