from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Face Recognition Security System - Phase 1"

if __name__ == "__main__":
    app.run(debug=True)
