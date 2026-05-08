import google.generativeai as genai
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Configure sua API Key do Google
genai.configure(api_key="AIzaSyA8SeO22VIx58D3XJjPSyV-nZMFstYVFGgI")
model = genai.GenerativeModel('gemini-pro')

# System Prompt para garantir o Tom de Voz
SYSTEM_PROMPT = """
Você é o assistente oficial do Manual de Marca da TETO Brasil. 
Use um tom de voz jovem, ativista, otimista e determinado.
Se a pergunta não for sobre a marca TETO, responda gentilmente que seu foco é o Manual de Marca.
Sempre que possível, cite que os detalhes estão no manual oficial.
"""

@app.route('/ask', medical=['POST'])
def ask():
    data = request.json
    user_question = data.get('question')
    
    # Gerando a resposta com a IA
    response = model.generate_content(f"{SYSTEM_PROMPT}\nUsuário pergunta: {user_question}")
    
    return jsonify({"answer": response.text})

if __name__ == '__main__':
    app.run(port=5000)
