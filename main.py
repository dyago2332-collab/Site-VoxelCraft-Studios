import os
from flask import Flask, send_from_directory

app = Flask(__name__)

@app.route("/")
def home():
    # Abre o seu arquivo index.html na página inicial
    return send_from_directory('.', 'index.html')

@app.route('/<path:path>')
def send_static(path):
    # Carrega as imagens, estilos e scripts das suas pastas
    return send_from_directory('.', path)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
