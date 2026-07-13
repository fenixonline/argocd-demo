from flask import Flask

app = Flask(__name__)

VERSION = "1.0.1"

@app.route("/")
def home():
    return f"Hello from ArgoCD Demo - Version {VERSION}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)