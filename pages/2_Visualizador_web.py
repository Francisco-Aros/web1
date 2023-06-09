import geopandas as gpd
import folium
from streamlit_folium import folium_static
import streamlit as st

st.set_page_config(
    page_title="Visualizador",
    page_icon=":globe_with_meridians:",
    layout="wide"
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

st.title("Ejemplo de capas de información en visualizador web")

st.info("En el siguiente mapa cuenta con un selector de capas para poder activar/desactivar las que desee. En este ejemplo se cuenta con los usos del suelo al año 2006 de lo que actualmente comprende el territorio de acción de la Asociación Paisajes de Conservación en la Región de Los Ríos.")

@st.cache_data() 
def get_data():
# Cargar el archivo SHP en un objeto GeoDataFrame
    shp_path = "USO_suelo_Valdivia2006.shp"
    gdf = gpd.read_file(shp_path)
    # Cargar el segundo archivo SHP en otro objeto GeoDataFrame
    shp2_path = "USO_suelo_LosLagos2006.shp"
    gdf2 = gpd.read_file(shp2_path)
    # Cargar el tercer archivo SHP en otro objeto GeoDataFrame
    shp3_path = "USO_suelo_Mafil_2006.shp"
    gdf3 = gpd.read_file(shp3_path)
    # Cargar el cuarto archivo SHP en otro objeto GeoDataFrame
    shp4_path = "USO_suelo_Panguipulli2006.shp"
    gdf4 = gpd.read_file(shp4_path)
    return gdf, gdf2, gdf3, gdf4



# Crear un objeto Folium Map centrado en los datos de los polígonos
m = folium.Map(location=[-39.8, -72.8], zoom_start=9)

# Función para asignar colores diferentes a cada atributo
def style_function(feature):
    attribute = feature['properties']['USO_ACTUAL']
    if attribute in ['B.Nat.Achaparrado Abierto','B.Nat.Achaparrado Semidenso', 'B.Nat.Adulto-Renoval Abierto', 'B.Nat.Adulto-Renoval Denso', 'B.Nat.Adulto-Renoval Semidenso', 'B.Nat-Exoticas Asilv.Semidenso', 'B.Nat-Exoticas Asilves.Abierto', 'B.Nat-Exoticas Asilves.Denso', 'B.Nativo-Plantacion Abierto', 'B.Nativo-Plantacion Semidenso', 'Bosque Nativo Adulto Abierto', 'Bosque Nativo Adulto Denso', 'Bosque Nativo Adulto Semidenso']:
        return {'fillColor': 'green', 'color': 'green'}
    elif attribute == 'Ciudades-Pueblos-Zonas.Indus.':
        return {'fillColor': 'red', 'color': 'red'}
    elif attribute in['Lago-Laguna-Embalse-Tranque', 'Nieves', 'Otros Terrenos Humedos', 'Playas y Dunas', 'Rios', 'Vegetacion Herbacea en Orilla']:
        return {'fillColor': 'blue', 'color': 'blue'}
    elif attribute in ['Matorral Abierto', 'Matorral Arborescen. Semidenso', 'Matorral Arborescente Abierto', 'Matorral Denso', 'Matorral Pradera Abierto', 'Matorral Semidenso', 'Praderas Perennes']:
        return {'fillColor': 'yellow', 'color': 'yellow'}
    elif attribute in ['Planta.Joven-Recien Cosechada', 'PLANTACION', 'Plantacion']:
        return {'fillColor': 'orange', 'color': 'orange'}
    elif attribute == 'Protecciones':
        return {'fillColor': 'sky blue', 'color': 'sky blue'}
    elif attribute in ['Renoval Abierto', 'Renoval Denso', 'Renoval Semidenso']:
        return {'fillColor': 'Dark Green', 'color': 'Dark Green'}
    else:
        return {'fillColor': 'gray', 'color': 'gray'}


# Agregar los datos de los polígonos al mapa
# Obtener los datos de los polígonos y agregarlos al mapa
gdf, gdf2, gdf3, gdf4 = get_data()

folium.GeoJson(gdf,
               name='Uso de suelo en Valdivia al año 2006',
               tooltip=folium.GeoJsonTooltip(fields=['COMUNA','USO_ACTUAL'], aliases=['Comuna', 'Uso de suelo al 2006']),
               style_function=style_function,
               show=False# no se moestrara la capa al cargar la página, de lo contrario si es que se desea que se pueda visualizar desde un inicio debe ser con el comando "overlay=True"
               ).add_to(m)

# Agregar los datos de los polígonos del segundo archivo SHP al mapa
folium.GeoJson(gdf2,
               name='Uso de suelo en Los Lagos al año 2006',
               tooltip=folium.GeoJsonTooltip(fields=['COMUNA','USO_ACTUAL'], aliases=['Comuna', 'Uso de suelo al 2006']),
               style_function=style_function,
               show=False# no se moestrara la capa al cargar la página, de lo contrario si es que se desea que se pueda visualizar desde un inicio debe ser con el comando "overlay=True"
               ).add_to(m)

#Agrega los datos de la tercera capa SHP al mapa
folium.GeoJson(gdf3,
               name='Uso de suelo en Máfil al año 2006',
               tooltip=folium.GeoJsonTooltip(fields=['COMUNA','USO_ACTUAL'], aliases=['Comuna','Uso de suelo al 2006']),
               style_function=style_function,
               show=False# no se moestrara la capa al cargar la página, de lo contrario si es que se desea que se pueda visualizar desde un inicio debe ser con el comando "overlay=True"
               ).add_to(m)

#Agrega los datos de la cuarta capa SHP al mapa
folium.GeoJson(gdf4,
               name='Uso de suelo en Panguipulli al año 2006',
               tooltip=folium.GeoJsonTooltip(fields=['COMUNA','USO_ACTUAL'], aliases=['Comuna','Uso de suelo al 2006']),
               style_function=style_function,
               show=False# no se moestrara la capa al cargar la página, de lo contrario si es que se desea que se pueda visualizar desde un inicio debe ser con el comando "overlay=True"
               ).add_to(m)


# Crear el control de capas agrupadas

control = folium.LayerControl()

control.add_to(m)


# Mostrar el mapa en Streamlit
folium_static(m)



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