# Proyecto: Conexión de WhatsApp con API local usando Twilio y ngrok

Este proyecto provee un **servicio de integración** que permite recibir mensajes de **WhatsApp** y redirigirlos a tu **API local** a través de **Twilio**. Para exponer tu servicio al exterior sin necesidad de desplegarlo en la nube, se utiliza **ngrok** como túnel seguro.

## 1. Descripción General

- **WhatsApp** envía los mensajes a Twilio.
- **Twilio** reenvía dichos mensajes a tu **API local** a través de ngrok.
- **Tu API local** procesa los mensajes y, opcionalmente, responde al usuario de WhatsApp a través de Twilio.

De esta forma, tu proyecto funge como un **puente de comunicación** entre usuarios de WhatsApp y tu aplicación.

## 2. Dependencias y Requisitos

1. **[Ollama 3.2](https://ollama.com/docs)**  
   Debes tener instalada la versión 3.2 de Ollama, ya que el proyecto se integra con un modelo local para procesar y/o generar texto (dependiendo de tu flujo).

2. **Python 3.x** y un gestor de paquetes como `pip`.

3. **Twilio**  
   Necesitas una cuenta de Twilio para enviar y recibir mensajes de WhatsApp.  
   - Obtén tus credenciales (`TWILIO_ACCOUNT_SID`, `TWILIO_AUTH_TOKEN`) en la consola de [Twilio](https://www.twilio.com/console).

4. **ngrok**  
   Instala [ngrok](https://ngrok.com/) para exponer tu API local a internet, permitiendo que Twilio envíe solicitudes a tu servidor.

5. **Archivo `.env`**  
   Se requiere un archivo `.env` con datos de configuración correctos para Twilio y otros parámetros, por ejemplo:
   ```bash
   TWILIO_ACCOUNT_SID=tu_account_sid
   TWILIO_AUTH_TOKEN=tu_auth_token
   TWILIO_PHONE_NUMBER=whatsapp:+14155238886
   WHATSAPP_PHONE_NUMBER=whatsapp:+1234567890
   TWILIO_STATUS_CALLBACK_URL=https://<ngrok_subdomain>.ngrok.io/status_callback
   # Configuración para Ollama, etc.
   ```

## 3. Instalación y Configuración

1. **Clonar el Repositorio**  
   ```bash
   git clone https://github.com/usuario/mi-proyecto-whatsapp.git
   cd mi-proyecto-whatsapp
   ```

2. **Crear y Activar un Entorno Virtual** (recomendado)  
   ```bash
   python -m venv venv
   source venv/bin/activate  # macOS/Linux
   # o venv\Scripts\activate en Windows
   ```

3. **Instalar Dependencias**  
   ```bash
   pip install -r requirements.txt
   ```
   (Asegúrate de editar el `requirements.txt` para incluir las librerías que uses, como `flask`, `requests`, `llama-index`, etc.)

4. **Instalar Ollama 3.2**  
   Sigue las instrucciones de [Ollama](https://ollama.com/docs) para instalar la versión **3.2**. Asegúrate de que Ollama esté correctamente configurada y puedas correr modelos localmente.

5. **Crear y Completar el Archivo `.env`**  
   Basándote en el ejemplo descrito más arriba, añade tus credenciales de Twilio y los datos necesarios:
   ```bash
   TWILIO_ACCOUNT_SID=ACxxxxxx
   TWILIO_AUTH_TOKEN=xxxxxx
   TWILIO_PHONE_NUMBER=whatsapp:+14155238886
   WHATSAPP_PHONE_NUMBER=whatsapp:+1234567890
   # Otras variables de entorno necesarias
   ```

## 4. Uso

1. **Iniciar el Modelo Local (Ollama)**  
   Ejecuta tu modelo con Ollama (por ejemplo):
   ```bash
   ollama run llama3.2
   ```
   Deja este proceso corriendo.

2. **Ejecutar la Aplicación**  
   ```bash
   python app.py
   ```
   Debería iniciar la aplicación Flask en el puerto `5000`.

3. **Exponer tu API con ngrok**  
   ```bash
   ngrok http http://127.0.0.1:5000
   ```
   Copia la URL generada por ngrok (por ejemplo `https://<subdominio>.ngrok.io`) y configúrala en Twilio (o en tu `.env` como `TWILIO_STATUS_CALLBACK_URL`) para que Twilio envíe los mensajes a `https://<subdominio>.ngrok.io/webhook`.

4. **Probar el Flujo**  
   - Envía un mensaje de WhatsApp al número configurado en Twilio.
   - Verifica en la consola de tu aplicación Flask que se reciben los mensajes y se responden adecuadamente.

## 5. Contribuciones

Mariano Grasso
Pablo Gómez
Lautaro Silva
