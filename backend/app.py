from flask import Flask
from flask_cors import CORS
from routes.combined_route import combined_bp

app = Flask(__name__)
CORS(app)
app.register_blueprint(combined_bp)

if __name__ == '__main__':
    app.run(debug=True)

