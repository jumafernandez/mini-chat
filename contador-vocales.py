import streamlit as st

def contar_vocales(texto):
    cantidad = 0
    vocales = "aeiouáéíóúAEIOUÁÉÍÓÚ"
    for c in texto:
        if c in vocales:
            cantidad += 1

    return cantidad

st.title("🔡 Contador de vocales")

texto = st.text_input("Escribí una palabra o frase:")

if st.button("Contar vocales"):
    if texto:
        cantidad = contar_vocales(texto)
        st.success(f"El texto contiene {cantidad} vocales.")
    else:
        st.warning("Por favor, ingresá algún texto.")
