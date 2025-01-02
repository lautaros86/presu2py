from flask import Flask, request, jsonify
from dotenv import load_dotenv
from OllamaService import process_message

from TwilioService import callTwilio

load_dotenv()
app = Flask(__name__)


@app.route("/webhook", methods=['POST'])
def webhook():
    # Obtener el mensaje de WhatsApp
    incoming_msg = request.form.get('Body', '').strip()
    from_number = request.form.get('From', '')
    try:
        response_msg = process_message(incoming_msg)
        try:
            callTwilio(response_msg)
        except Exception as e:
            return "Sorry, something went wrong with Twilio service."
    except Exception as e:
        return "Sorry, something went wrong with the AI service."

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
