from flask import Flask, request, jsonify
from twilio.rest import Client
from dotenv import load_dotenv
from transformers import pipeline

import os

load_dotenv()

app = Flask(__name__)

# Configuración de Twilio
client = Client(os.getenv('TWILIO_ACCOUNT_SID'), os.getenv('TWILIO_AUTH_TOKEN'))

# Cargar el modelo de Hugging Face
generator = pipeline('text-classification')  # O usa 'EleutherAI/gpt-neo-1.3B' para otro modelo

@app.route("/webhook", methods=['POST'])
def webhook():
    # Obtener el mensaje de WhatsApp
    incoming_msg = request.form.get('Body', '').strip()
    from_number = request.form.get('From', '')

    # Generar una respuesta usando el modelo de Hugging Face
    try:
        # Usar el modelo de Hugging Face para generar una respuesta
        response = generator(incoming_msg, max_length=150, num_return_sequences=1)

        # Obtener el texto generado
        response_msg = response[0]['generated_text'].strip()

    except Exception as e:
        response_msg = "Sorry, something went wrong with the AI service."

    # Enviar la respuesta a través de Twilio
    message = client.messages.create(
        body=response_msg,
        from_=os.getenv('TWILIO_PHONE_NUMBER'),
        to=os.getenv('WHATSAPP_PHONE_NUMBER')
    )

    return jsonify({'status': 'Message sent'}), 200

# Nuevo endpoint para manejar status callbacks
@app.route("/status-callback", methods=['POST'])
def status_callback():
    print("Status callback recibido")
    # Obtener datos del callback
    message_sid = request.form.get('MessageSid')
    message_status = request.form.get('MessageStatus')
    error_code = request.form.get('ErrorCode')
    error_message = request.form.get('ErrorMessage')

    # Aquí puedes procesar los datos como desees
    # Por ejemplo, registrar en logs o base de datos
   # app.logger.info(f"SID: {message_sid}, Status: {message_status}, Error Code: {error_code}, Error Message: {error_message}")
    print(f"SID: {message_sid}, Status: {message_status}, Error Code: {error_code}, Error Message: {error_message}")

    return '', 204  # Responder con 204 No Content


if __name__ == "__main__":
    app.run(debug=True)
