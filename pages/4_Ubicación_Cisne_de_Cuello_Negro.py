import pydeck as pdk
import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(
    page_icon=":thumbs_up:",
    layout="wide",
)

st.sidebar.write("")
st.sidebar.write("")
st.sidebar.write("")
st.sidebar.write("")
st.sidebar.write("")
st.sidebar.write("")
st.sidebar.write("")
st.sidebar.write("")
st.sidebar.write("")
st.sidebar.write("")
st.sidebar.write("")

# Crea dos columnas en el sidebar
col1, col2 = st.sidebar.columns([1,7])

# Agrega contenido a la primera columna
col1.image("gmail.png", width=25)
col1.image("linkedin.png", width=25)

# Agrega contenido a la segunda columna
col2.write("[Contacto](mailto:franciscoarosmunoz@gmail.com)")
col2.write("[Sígueme](https://www.linkedin.com/in/francisco-aros-muñoz/)")





css = '''
<style>
    [data-testid='stSidebarNav'] > ul {
        min-height: 54vh;
    }
</style>
'''

st.markdown(css, unsafe_allow_html=True)


@st.cache_data
def carga_data():
  return pd.read_excel("Cuello_negro(1).xlsx", header=0)



ciudad = carga_data()
ciudad["Fecha_de_Proceso"] = "25-05-2023"

st.title("Avistamientos de Cisnes de Cuello Negro en Chile y Argentina.")
st.write("Para el caso de los cisnes de cuello negro, también se ha decidido poner enfasís en los avistamientos históricos tan solo en lo que son los territorio de Chile y Argentina, lo cual no significa que no existan avistamientos de esta especie en otras localidades en otros países, es más, si uno realiza una búsqueda en GBIF, puede encontrar una inmensa base de datos con gran cantidad de información detallada sobre sus avistamientos.")
geo_puntos_visual = ciudad[["kingdom", "phylum", "class", "order", "family", "genus", "species", "scientificName", "countryCode", "decimalLatitude", "decimalLongitude", "eventDate", "day","month", "year", "basisOfRecord", "Fecha_de_Proceso"]].rename(columns={
    "kingdom": "Reino",
    "phylum": "Phylum",
    "class": "Clase",
    "order": "Orden",
    "family": "Familia",
    "genus": "Genus",
    "species": "Especie",
    "scientificName": "Nombre_Cientifico",
    "countryCode": "Código_del_país",
    "decimalLatitude": "Latitud",
    "decimalLongitude": "Longitud",
    "eventDate": "Fecha_avistamiento",
    "day": "Día",
    "month": "Mes",
    "year": "Año",
    "basisOfRecord": "Tipo_registro"
})

#Para una correcta visualización de los puntos en el mapa a generar se deben eliminar las celdas sin registros, TODAS LAS CELDAS
#Lo anterior se realiza con agregando la función Nombre_DataFrame.dropna(subset=["Campos sin registros separados por una coma"], inplace=True)
geo_puntos_visual.dropna(subset=["Latitud", "Longitud", "Año", "Día"], inplace=True)
geo_data = geo_puntos_visual

geo_data["Fecha_de_Proceso"] = "03-05-2023"

st.markdown("#### Avistamiento de Chucaos en Chile.")
col_sel, col_map = st.columns([1, 2])

with col_sel:
  # Obtener los nombres unicos por mes
  Visualizacion = geo_puntos_visual["Mes"].sort_values().unique()

  visualizacion_seleccionada = st.multiselect(
    label="Filtrar por Mes de avistamiento", 
    options=Visualizacion,
    help="Selecciona el o los meses de avistamiento que desea visualizar",
    default=[] # También se puede indicar la variable "comunas", para llenar el listado
  )

  # Obtener los nombres unicos por mes
  Visualizacion = geo_puntos_visual["Año"].sort_values().unique()

  visualizacion_seleccionada2 = st.multiselect(
    label="Filtrar por Año de avistamiento", 
    options=Visualizacion,
    help="Selecciona el o los años de avistamiento que desea visualizar",
    default=[] # También se puede indicar la variable "comunas", para llenar el listado
  )
# Obtener los nombres unicos por mes
  Visualizacion = geo_puntos_visual["Código_del_país"].sort_values().unique()

  visualizacion_seleccionada3 = st.multiselect(
    label="Filtrar por País de avistamiento", 
    options=Visualizacion,
    help="Selecciona el o los países de avistamiento que desea visualizar",
    default=[] # También se puede indicar la variable "comunas", para llenar el listado
  )
  #st.write(geo_data.set_index("Año"))
  st.write("A continuación y al igual que para el caso de los Chucas, podrán realizar hasta tres filtros con el fin de obtener una visualización más detallada según los requerimientos de cada uno, cabe señalar que estos filtros pueden ser combinados entre sí. En caso de no existir un filtro seleccionado, se mostrarán la totalidad de los puntos de avistamientos.")


geo_data = geo_puntos_visual

# Aplicar filtro de Mes
if visualizacion_seleccionada:
  geo_data = geo_puntos_visual.query("Mes == @visualizacion_seleccionada")

#Aplicar filtro de año
if visualizacion_seleccionada2:
  geo_data = geo_puntos_visual.query("Año == @visualizacion_seleccionada2")

#Aplicar filtro de país
if visualizacion_seleccionada3:
   geo_data = geo_puntos_visual.query("Código_del_país == @visualizacion_seleccionada3")

#Aplicar ambos filtros al mismo tiempo
if visualizacion_seleccionada and visualizacion_seleccionada2 and visualizacion_seleccionada3:
  geo_data = geo_puntos_visual[geo_puntos_visual['Mes'].isin(visualizacion_seleccionada) & geo_puntos_visual['Año'].isin(visualizacion_seleccionada2) & geo_puntos_visual['Código_del_país'].isin(visualizacion_seleccionada3)]


avg_lat = np.median(geo_data["Latitud"])
avg_lng = np.median(geo_data["Longitud"])

puntos_mapa = pdk.Deck(
    map_style='road',
    initial_view_state=pdk.ViewState(
        latitude=avg_lat,
        longitude=avg_lng,
        zoom=5.2,
        min_zoom=1,
        max_zoom=15,
        pitch=10,
    ),
    layers=[
        pdk.Layer(
            "ScatterplotLayer",
            data=geo_data,
            pickable=True,
            auto_highlight=True,
            get_position='[Longitud, Latitud]',
            filled=True,
            opacity=0.5,
            radius_scale=20,
            radius_min_pixels=3,
            get_fill_color=["Código_del_país == 'AR' ? 200 : 20", "Código_del_país == 'CL' ? 100 : 20", 60, 230]
        ),
    ],
    tooltip={
        "html": "<b> Mes de avistamiento: </b> {Mes} <br/>"
                "<b> Año de avistamiento: </b>{Año} <br/>"
                "<b> País de avistamiento (código): </b>{Código_del_país} <br/>"
                "<b> Especie: </b> {Especie} <br/>"
                "<b> Tipo de registro: </b> {Tipo_registro} <br/>"
                "<b> Georreferencia (Lat, Lng): </b> [{Latitud}, {Longitud}] <br/>"
    }
)



with col_map:
    st.write(puntos_mapa)


st.write("A su vez, también existe una diferenciación entre los avistamientos realizados en Chile y los que se encuentran en Argentina, diferenciandose por colores, con el fin de poder crear una mejor experiencia al momento de navegar por el mapa desarrollado. ")
st.write("Si desea poder descargar la información con la cual se ha trabajado esta web, la cual cuenta con toda la información que usted puede apreciar al momento de navegar por el mapa web, pulse en el siguiente enlace:")

# define una función para descargar el DataFrame como un archivo Excel
def descargar_excel():
    output = pd.ExcelWriter('cuello_negro.xlsx')
    geo_puntos_visual.to_excel(output)
    output.close()
    with open('cuello_negro.xlsx', 'rb') as f:
        archivo_excel = f.read()
    return 'cuello_negro.xlsx' #archivo_excel

# crea un botón de descarga personalizado que llama a la función de descarga
boton_descarga = st.download_button(
    label='Descargar de datos.',
    data=descargar_excel,
    file_name='cuello_negro.xlsx'
)

# muestra el botón de descarga en la aplicación de Streamlit
st.write(boton_descarga, unsafe_allow_html=True)

st.markdown("<h3 id='referencias'>Referencias</h3>", unsafe_allow_html=True)
st.write("GBIF.org (07 May 2023) GBIF Occurrence Download  https://doi.org/10.15468/dl.tjt6fu")


def main():
# Estilo CSS para anclar en la parte inferior
    st.markdown(
            """
            <style>
            .footer {
                position: fixed;
                left: 0;
                bottom: 0;
                width: 100%;
                background-color: #000000;
                padding: 2px;
                text-align: center;
            }
            .footer p {
            font-size: 12px; /* Ajusta el tamaño de la letra */
            line-height: 1.2; /* Ajusta el espacio entre líneas */
            margin: 0; /* Elimina el margen alrededor del párrafo */
            color: #ffffff; /* Cambia el color del texto a blanco */
            }
            .footer a {
            font-size: 15px; /* Ajusta el tamaño del hipervínculo */
            color: #1443E4; /* Cambia el color del hipervínculo a blanco */
            }
            </style>
            """,
            unsafe_allow_html=True
        )

        # Agrega una división con la clase 'footer'
    st.markdown(
            """
            <div class="footer">
                <p>Web diseñada y desarrollada por Francisco Javier Aros Muñoz</p>
                <a href="mailto:franciscoarosmunoz@gmail.com">franciscoarosmunoz@gmail.com</a>
            </div>
            """,
            unsafe_allow_html=True
        )
    
if __name__ == '__main__':
    main()