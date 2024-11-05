import streamlit as  st


home = st.Page(
    page="vistas/home.py",
    title="Inicio",
    icon="🏠",
    default=True
)

acerca_de = st.Page(
    page="vistas/acerca_de.py",
    title="Aerca de",
    icon=":material/account_circle:",
)

project_1_page = st.Page(
    page="vistas/ventas.py",
    title="Ventas",
    icon = "🛒"
)

project_2_page= st.Page(
    page="vistas/chatbot.py",
    title="Chatbot",
    icon="🤖"
)

pg = st.navigation(
    {
        "Información: ":[home, acerca_de],
        "Proyector: ": [project_1_page, project_2_page]
    }
)

#  NAVEGACION 
pg.run()


