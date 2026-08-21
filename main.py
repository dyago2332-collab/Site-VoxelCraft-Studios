import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Meu site Python está no ar pelo Google!</h1>"

if __name__ == "__main__":
    # O Google Cloud define a porta automaticamente através da variável PORT
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
