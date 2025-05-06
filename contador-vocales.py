import streamlit as st

def contar_vocales(texto):
    vocales = "aeiouáéíóúAEIOUÁÉÍÓÚ"
    return sum(1 for c in texto if c in vocales)

st.title("🔡 Contador de vocales")

texto = st.text_input("Escribí una palabra o frase:")

if st.button("Contar vocales"):
    if texto:
        cantidad = contar_vocales(texto)
        st.success(f"El texto contiene {cantidad} vocales.")
    else:
        st.warning("Por favor, ingresá algún texto.")
