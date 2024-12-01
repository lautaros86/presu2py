from flask import Flask, request, jsonify
from twilio.rest import Client
import os

app = Flask(__name__)

client = Client(os.getenv('TWILIO_ACCOUNT_SID'), os.getenv('TWILIO_AUTH_TOKEN'))

@app.route("/webhook", methods=['POST'])
def webhook():
    # Obtener el mensaje de WhatsApp
    incoming_msg = request.form.get('Body', '').strip()
    from_number = request.form.get('From', '')

    # Responder con un mensaje
    response_msg = "Hi, how can I help you? 3"

    # Enviar respuesta
    message = client.messages.create(
        body=response_msg,
        from_=os.getenv('TWILIO_PHONE_NUMBER'),
        to=os.getenv('WHATSAPP_PHONE_NUMBER')
    )

    return jsonify({'status': 'Message sent'}), 200

if __name__ == "__main__":
    app.run(debug=True)
