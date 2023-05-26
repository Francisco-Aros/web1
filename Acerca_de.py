import streamlit as st
import streamlit.components.v1 as components


#Configuración inicial de la página
st.set_page_config(
    page_icon=":thumbs_up:",
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

st.title("Acerca de")
st.markdown("Me presento, mi nombre es Francisco Javier Aros Muñoz, Geógrafo egresado de la Universidad Austral de Chile en su sede de Valdivia y Magister en Planificación y Gestión Territorial de la Universidad Católica de Temuco.")

col_pic, col_descr = st.columns([1, 4])

with col_pic:
    # Cargar imagen desde el archivo seleccionado
    def main():
    # Ruta de la imagen que deseas mostrar
        image_path = "DSC_8357(1).jpg"
    # Mostrar la imagen en Streamlit
        st.image(image_path, caption='', use_column_width=True)

    if __name__ == "__main__":
        main()

with col_descr:
    st.write("Dentro de mi labor profesional he colaborado con distintas instituciones tanto en la Región de Los Ríos como en otras zonas del país, de forma presencial y telemática. Dentro de las más destacadas se encuentran los siguiente:")
    st.write("Servicio País en la comuna de María Pinto, Región Metropolitana año 2021.")
    st.write("Colaborador en Instituto Nacional de Estadísticas en la Región de Los Ríos en dos oportunidades, la primera como enumerador para el proyecto de actualización cartográfica de CASEN en el año 2022 y la segunda como encargado de grupo para el proyecto de Actualización Pre Censal año 2023.")
    st.write("También durante el año 2022 me desempeñé como Geógrafo en la Asociación de Municipalidades Paisajes de Conservación para la Biodiversidad de la Región de Los Ríos.")
    st.write("Finalmente, he desempeñado labores realizando pequeñas colaboraciones en proyectos que requerían de un geógrafo con el fin de plasmar información geoespacial en un tipo de archivo en específico, en una cartografía o base de datos solicitado.")

st.write("")
st.write("")




# Crea cuatro columnas
#col1, col2, col_3, col_4 = st.columns([1,11,1,11])

# Agrega contenido a las columnas
#col1.image("gmail.png", width=25)
#col2.write("[franciscoarosmunoz@gmail.com](mailto:franciscoarosmunoz@gmail.com)")
#col_3.image("linkedin.png", width=25)
#col_4.write("[Sígueme](https://www.linkedin.com/in/francisco-aros-muñoz/)")


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