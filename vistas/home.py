import streamlit as  st

#Inicio de pagina
with st.container():
    st.subheader("Bienvenido, Somos SOFIA👋😊")
    st.title("Creamos soluciones para acelerar tu negocio")
    st.write(
        "Somos unos apasionados de las tenologías y la innovación, especialización en el sector de la digitalización y automatización de negocios. Nos gusta crear soluciones para resolver problemas y mejorar procesos. "
    )
    st.write("[Saber más>](https://streamlit.io/)"
    )

#Sobre nosostros
with st.container():
    st.write("---")

    texto_columna, imagen_columna = st.columns((1,2))
    with texto_columna:
        st.subheader("Sobre nosotros 🔍⭐⭐")
        st.write(
            """
            Nuestro objetivo es poder aportar valor a los negocios ayudandoles a ahorrar tiempo y dinero a través de la implantación de nuevas tecnologías como la inteligencia artifical, analisis de datos o implantación de software de automatización.

Seguramente te vamos a poder ayudar si:

-Tienes un negocio y quieres mejorar tus procesos de trabajo para ahorrar tiempo y dinero Tienes trabajadores que emplean parte de su jornada a realizar tareas repetitivas sin valor añadido

para tu negocio

No tienes claras las métricas de tu negocio y quieres tomar decisiones basadas en datos

-Quieres mejorar la experiencia de tus clientes

Usas herramientas de software antiguas o poco eficientes o procesos en los que usas papel y boligrafo

***Si esto suena interesante para ti puedes contactarnos a través del formulario que encontrarás al final de la página***

            """
    )
    with imagen_columna:
        st.image("img/\desarrolloApp.png")
    

#Servicios

with st.container():
    st.write("---")
    st.header("Servicios 👩‍💻👨‍💻")


    texto_columna, imagen_columna = st.columns((1,2))


with texto_columna:
    st.subheader("Diseño de aplicaciones")

    st.write(
        """
        Si en tus procesos diarios tienes que introducir información en diferentes fuentes de datos o bien tienes que 
        trabajar con documentación en papel, es hora de pensar en implementar una aplicación en tu negocio para potenciar y optimizar el funcionamiento de los procesos diarias
        """
    )
    st.write("[Ver servicios >](https://streamlit.io/)")
    
    with imagen_columna: st.image("img/image.png")