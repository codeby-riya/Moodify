from flask import Flask
from flask_cors import CORS
from routes.combined_route import combined_bp
import os

app = Flask(__name__)

# Allow requests from your React frontend (localhost during testing)
CORS(app, origins=["https://moodify-jet.vercel.app"], supports_credentials=True)


# Register combined route from your ML logic
app.register_blueprint(combined_bp)

# Basic route to check server status
@app.route('/')
def index():
    return "Moodify backend is running"

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
