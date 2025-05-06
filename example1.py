import streamlit as st

st.title("Mi primera app")
nombre = st.text_input("¿Cómo te llamás?")
if st.button("Saludar"):
    st.write(f"Hola, {nombre} 👋")
