import streamlit as st
from forms.contacto import contact_form

#Ventana modal
@st.dialog("contacto")
def ver_form_contacto():
    contact_form()

col1, col2 = st.columns(2, gap=small, vertical_alignment=center)
with col1:
    st.image(img/Oscar.jpg, width=230)
with col2:
        st.title("Oscar Martínez", anchor=False)
        st.write(
"Analista de datos senior, que ayuda a las empresas apoyando la toma de decisiones basada en datos. Como Ciencia de Datos"
)

if st.button(Contacto): # Mostrar botón ventana modal
    ver_form_contacto()

# --- Experiencia y calificaciones ---
    st.write("\n")
    st.subheader("Experiencia y calificaciones", anchor=False)
    st.write(
"""
- 7 años de experiencia extrayendo información útil a partir de datos.
- Fuerte experiencia práctica y conocimiento en Python y Excel.
- Buen conocimiento de los principios estadísticos y sus respectivas aplicaciones.
- Excelente jugador de equipo y con un fuerte sentido de iniciativa en las tareas.
"""
)
# --- HABILIDADES ---
    st.write("\n")
    st.subheader("Habilidades", anchor=False)
    st.write(
    """
- Programación: Python (Scikit-learn, Pandas), SQL, VBA
- Visualización de Datos: PowerBi, MS Excel, Plotly
- Modelado: Logistic regression, linear regression, decision trees
- Base de Datos: Postgres, MongoDB, MySQL
"""
)

Contacto.py
import re
import time
import streamlit as st

def is_valid_email(email):
    email_pattern=r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(email_pattern, email) is not None

def contact_form():
    with st.form("contact_form"):
        name = st.text_input("Nombres y Apellidos.")
        email = st.text_input("Correo electrónico:")
        message = st.text_area("Su Mensaje:")
        submit_button = st.form_submit_button("Enviar")

if submit_button:
        
        if not name:
            st.error("Por favor escriba su nombre.", icon="🧑")
            st.stop()

        if not email:
            st.error("Por favor escriba su dirección de correo electrónico.", icon="📨")
            st.stop()

if not is_valid_email(email):
            st.error("Por favor su dirección de correo electrónico no es correcto.", icon="📧")
            st.stop()

if not message:
            st.error("Por favor escriba un mensaje.", icon="💬")
            st.stop()

if submit_button: 
            st.success("Se envio satisfactoriamente.", icon="✅")
            time.sleep(2)
            st.rerun()


st.title("acerca de")