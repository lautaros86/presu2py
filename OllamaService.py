from ollama import ChatResponse, Client as OllamaClient

# Configuración de Ollama
oLlamaClient = OllamaClient(
    host='http://localhost:11434',
    headers={'x-some-header': 'some-value'}
)

conversation_history = []

def process_message(user_msg):
    # 1. Guardar el mensaje del usuario en la lista
    conversation_history.append({"role": "user", "content": user_msg})

    # 2. Construir el prompt completo
    prompt = build_prompt(conversation_history)

    # 3. Llamar a Ollama (con tu wrapper o API) usando todo el prompt
    response_text = call_ollama(prompt)

    # 4. Agregar respuesta al historial
    conversation_history.append({"role": "assistant", "content": response_text})

    return response_text

def build_prompt(conversation):
    # Construir prompt concatenando user/assistant
    # "User: Hola\nAssistant: Hola, ¿en qué te ayudo?\nUser: Cuéntame más\nAssistant:"
    lines = []
    for turn in conversation:
        role = "User" if turn["role"] == "user" else "Assistant"
        lines.append(f"{role}: {turn['content']}")
    # Agregamos un "Assistant:" final para que el modelo responda
    lines.append("Assistant:")
    return "\n".join(lines)

def call_ollama(prompt):
    # Generar una respuesta usando el modelo de Hugging Face
    # Usar el modelo de llama para generar una respuesta
    response: ChatResponse = oLlamaClient.chat(model='llama3.2', messages=[
        {
            'role': 'user',
            'content': prompt,
        },
    ])

    if (len(response.message.content) > 1550):
        response: ChatResponse = oLlamaClient.chat(model='llama3.2', messages=[
            {
                'role': 'user',
                'content': prompt + ". responde en menos de 1500 caracteres",
            },
        ])
    # Obtener el texto generado
    return response.message.content

