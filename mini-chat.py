import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import os

# Cargar la API Key desde .env
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# Inicializar el cliente
client = OpenAI(api_key=api_key)

# Configuración de la página
st.set_page_config(page_title="Mini Chat-GPT", page_icon="💬", layout="centered")

st.markdown("## 💬 Mini Chat-GPT")
st.markdown("Escribí un mensaje y presioná enviar para hablar con un modelo de lenguaje.")

# Input del usuario
prompt = st.text_area("✍️ Tu mensaje", height=100, placeholder="Ej: ¿Cómo se calcula la sucesión de Fibonacci?")

# Botón
if st.button("Enviar"):
    if not prompt.strip():
        st.warning("Por favor, escribí algo antes de enviar.")
    else:
        with st.spinner("Generando respuesta..."):
            try:
                response = client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "user", "content": prompt}
                    ],
                    temperature=0.7,
                    max_tokens=500
                )
                reply = response.choices[0].message.content
                st.markdown("### 🤖 Respuesta del modelo:")
                st.success(reply)
            except Exception as e:
                st.error(f"Error al generar respuesta: {e}")
