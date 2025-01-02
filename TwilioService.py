import os
from twilio.rest import Client as TwilioClient

# Configuración de Twilio
twilioClient = TwilioClient(os.getenv('TWILIO_ACCOUNT_SID'), os.getenv('TWILIO_AUTH_TOKEN'))


def callTwilio(body):
        # Enviar la respuesta a través de Twilio
        return twilioClient.messages.create(
            body=body,
            from_=os.getenv('TWILIO_PHONE_NUMBER'),
            to=os.getenv('WHATSAPP_PHONE_NUMBER')
        )


