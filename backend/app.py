from flask import Flask, request, jsonify
from flask_cors import CORS
from routes.combined_route import combined_bp
import os

app = Flask(__name__)

# Allow both frontend and localhost access during testing
CORS(app, origins=[
    "https://moodify-jet.vercel.app",  # Vercel frontend
    "http://localhost:3000"            # Local frontend
], supports_credentials=True)

# Register your route logic
app.register_blueprint(combined_bp)

# Optional health check route
@app.route('/')
def index():
    return "Moodify backend is running ✅"

# Run the server
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
