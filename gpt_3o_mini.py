import openai
import os

# Cargar la API Key desde la variable de entorno (asegúrate de configurarla en tu sistema)
#os.getenv
openai.api_key = ("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")

def generate_text(prompt, chat_history, language="es"):
    try:
        client = openai.OpenAI()  # ✅ Nueva forma de inicializar el cliente
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",  # O usa "gpt-3.5-turbo" o "gpt-4-turbo" si tienes acceso
            messages=[
                {"role": "system", "content": "Eres un asistente de inversiones."},
                * [{"role": "user", "content": msg} for msg in chat_history],  # Historial de conversación
                {"role": "user", "content": prompt}
            ],
            max_tokens=400
        )
        return response.choices[0].message.content
    
    except openai.OpenAIError as e:
        return f"Error al generar respuesta: {str(e)}"
    
    