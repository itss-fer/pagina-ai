from flask import Flask, request, render_template, redirect, url_for
import openai
import os
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

# Configurar OpenAI
openai.api_key = os.getenv("OPENAI_API_KEY")

# Crear la aplicación Flask
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    user_message = request.form.get('message')

    # Configura el modelo y parámetros para OpenAI
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=user_message,
        max_tokens=150
    )

    # Extraer la respuesta
    answer = response.choices[0].text.strip()

    return render_template('index.html', response=answer)

if __name__ == '__main__':
    app.run(debug=True)
