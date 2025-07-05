from flask import Flask
from flask_cors import CORS
from routes.combined_route import combined_bp
from deepface import DeepFace
import os

app = Flask(__name__)
CORS(app, origins=["https://moodify-jet.vercel.app"], supports_credentials=True)
app.register_blueprint(combined_bp)

DeepFace.build_model("Emotion")

@app.route('/')
def index():
    return "Moodify backend is running"

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
