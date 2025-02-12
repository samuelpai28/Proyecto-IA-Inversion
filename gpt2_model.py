from transformers import GPT2LMHeadModel, GPT2Tokenizer
import langdetect  # Biblioteca para detectar el idioma

# Cargar el modelo y el tokenizador
model_name = "gpt2"
model = GPT2LMHeadModel.from_pretrained(model_name)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)

def detect_language(text):
    """Detecta el idioma del texto usando langdetect."""
    try:
        return langdetect.detect(text)
    except:
        return "es"  # Si falla, asumir español por defecto

def generate_text(prompt, chat_history=None, temperature=0.7, top_k=50, top_p=0.9, max_length=150):
    """Genera una respuesta basada en el prompt y el historial de conversación."""
    
    # Detectar el idioma del prompt
    language = detect_language(prompt)

    # Construir el prompt con contexto previo
    if chat_history:
        context = " ".join(chat_history[-3:])  # Usar las últimas 3 interacciones como contexto
    else:
        context = ""

    # Definir prefijo según el idioma detectado
    if language == "en":
        full_prompt = f"Context: {context} User (English): {prompt} Assistant (English):"
    else:
        full_prompt = f"Contexto: {context} Usuario (Español): {prompt} Asistente (Español):"

    # Tokenizar con límite de longitud
    inputs = tokenizer(full_prompt, return_tensors="pt", truncation=True, max_length=500)

    # Generar texto
    outputs = model.generate(
        inputs["input_ids"],
        max_length=300,
        temperature=0.5,
        top_k=50,
        top_p=0.8,
        num_return_sequences=1,
        no_repeat_ngram_size=2,
        do_sample=True
    )

    return tokenizer.decode(outputs[0], skip_special_tokens=True)