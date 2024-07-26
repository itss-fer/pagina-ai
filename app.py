from flask import Flask, request, jsonify, render_template
import openai
import os
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

# Configurar OpenAI
openai.api_key = os.getenv("OPENAI_API_KEY")

# Crear la aplicación Flask
app = Flask(__name__)

# Reemplaza con tu ID de asistente
ASSISTANT_ID = "asst_7AIYSnPimhTxKB7H7ppZAhrr"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/cortana-api', methods=['POST'])
def cortana_api():
    data = request.get_json()
    user_question = data.get('question')

    # Consultar la API de OpenAI con el ID de asistente
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an assistant."},
            {"role": "user", "content": user_question}
        ],
        assistant_id=ASSISTANT_ID
    )

    # Extraer la respuesta
    answer = response.choices[0].message['content'].strip()

    # Devolver la respuesta como JSON
    return jsonify({'response': answer})

if __name__ == '__main__':
    app.run(debug=True)
