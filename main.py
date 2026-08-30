import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    # Isso vai fazer o Flask carregar o seu arquivo index.html real
    return render_template("index.html")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
