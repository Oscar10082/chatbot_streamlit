import streamlit as  st
from streamlit_lottie import st_lottie
import requests
import json

def get(path:str):
    with open(path, "r") as p:
        return json.load(p)

def get_url(url:str):
    r = requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()

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
    st.write("[Más sobre nosotros >](https://streamlit.io/)")
    

#Servicios

with st.container():
    st.write("---")
    st.header("Servicios")
#st.write("##")
    imagen_columna, texto_columna = st.columns((1,2))
    with imagen_columna:
        st.image("img/diseño.jpg")

with texto_columna:
    st.subheader("Diseño de aplicaciones")
    st.write(
"""
Si en tus procesos diarios tienes que introducir información en diferentes fuentes de datos o
bien tienes que trabajar con documentación en papel, es hora de pensar en implementar una
aplicación en tu negocio para potenciar y optimizar el funcionamiento de los procesos diarios.
"""
)
    st.write("[Ver servicios > ](https://streamlit.io/)")

with st.container():
    st.write("---")
    #st.write("##")
    imagen_columna, texto_columna = st.columns((1,2))

with imagen_columna:
    st.image("img/proceso.jpg")

with texto_columna:
    st.subheader("Automatización de procesos")
    st.write(
"""
Si realizas cualquier tipo de tarea repetitiva como por ejemplo introducir datos en excel u otras
aplicaciones, gestión de facturas, envío de emails a proveedores etc Lo que quizás necesitas es una
automatización de tareas para poder liberar recursos de esas actividades y poder emplearlos en otras
tareas más productivas.
"""
)
    st.write("[Ver servicios > ](https://streamlit.io/)")

with st.container():
    st.write("---")
#st.write("##")
    imagen_columna, texto_columna = st.columns((1,2))
with imagen_columna:
    st.image("img/datos.jpg")
with texto_columna:
    st.subheader("Visualización de datos")
    st.write(
"""
Si sientes que no tienes una visión clara de datos de tu negocio lo que necesitas es una
aplicación en la que puedas tener toda la información de interes de tu empresa.
"""
)
    st.write("[Ver servicios >](https://streamlit.io/)")
#contactos
with st.container():
    st.write("---")
c_columna, inf_columna = st.columns((1,2))
with c_columna:
    st.subheader("📧Contactos")
#https://formsubmit.co/
#https://www.w3schools.com/howto/howto_css_contact_form.asp
contacto_form = """
<form action="https://formsubmit.co/manzanaresdionicio@gmail.com" method="POST">
<input type="hidden" name="_captcha" value="false">
<input type="text" name="name" placeholder="Escriba su nombre" required>

<input type="email" name="email" placeholder="nombre@email.com" required>
<textarea name="message" placeholder="Su mensajes"></textarea>
<button type="submit">Enviar...</button>
</form>
"""
st.markdown(contacto_form, unsafe_allow_html=True)