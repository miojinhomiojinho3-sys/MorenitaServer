import os
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Servidor da Morenita online!"

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    mensagem = data.get("msg", "")
    jogador = data.get("player", "Jogador")

    resposta = f"Olá {jogador}! Eu sou a Morenita 😊 Você disse: {mensagem}"
    return jsonify({"reply": resposta})

if __name__ == "__main__":
    # Render define a porta automaticamente via variável de ambiente
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
