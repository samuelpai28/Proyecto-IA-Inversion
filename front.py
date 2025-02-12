import streamlit as st
from gpt_3o_mini import generate_text  # Importa la función de la API de OpenAI
from langdetect import detect


# Configuración de la página
st.set_page_config(page_title="AGENT", page_icon="💰" )
#layout="wide"

# Función para cargar el CSS externo
def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Cargar estilos desde styles.css
load_css("styles.css")

# Mostrar imagen de encabezado
st.image("C:/Users/Windows/Desktop/Proyecto_de_grado/Agent.webp", use_container_width=True)  # Asegúrate de que la imagen está en la misma carpeta

# Título de la aplicación
st.title("📈💎 Asistente Virtual de Inversiones")

# Respuestas rápidas para saludos y preguntas básicas en español e inglés
quick_responses = {
    "hola": "¡Hola! ¿Cómo puedo ayudarte hoy?",
    "hello": "Hello! How can I assist you today?",
    "buenos días": "¡Buenos días! ¿En qué te puedo ayudar?",
    "good morning": "Good morning! How can I assist you?",
    "adiós": "¡Hasta pronto!",
    "goodbye": "Goodbye! See you soon!",
    "gracias": "¡De nada! ¿Necesitas ayuda con algo más?",
    "thank you": "You're welcome! Need any further assistance?",
    "qué es una inversión": "Una inversión es el acto de destinar recursos con la expectativa de obtener un beneficio futuro.",
    "what is an investment": "An investment is the act of allocating resources with the expectation of generating a future profit.",
    "cómo invertir": "Para invertir, primero define tus objetivos financieros y elige activos adecuados como acciones, bonos o bienes raíces.",
    "how to invest": "To invest, first define your financial goals and choose suitable assets like stocks, bonds, or real estate."
}

# Estado de sesión para historial de conversación
if "messages" not in st.session_state:
    st.session_state.messages = []

# Mostrar historial de conversación
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Capturar input del usuario
if user_input := st.chat_input("Escribe tu pregunta aquí..."):
    with st.chat_message("user"):
        st.markdown(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Intentar detectar el idioma de la pregunta
    try:
        language = detect(user_input)
    except:
        language = "es"  # Si hay error, asumir español por defecto
    
    # Verificar si hay una respuesta rápida predefinida
    response = quick_responses.get(user_input.lower())

    # Si no hay respuesta rápida, generar con IA
    if not response:
        chat_history = [msg["content"] for msg in st.session_state.messages if msg["role"] == "user"]
        response = generate_text(user_input, chat_history, language)
        
        # Si la IA no genera respuesta, mostrar un mensaje amigable
        if not response.strip():
            response = "Lo siento, no tengo una respuesta para eso en este momento. ¿Puedes reformular tu pregunta?"
    
    # Mostrar respuesta del asistente
    with st.chat_message("assistant"):
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})
