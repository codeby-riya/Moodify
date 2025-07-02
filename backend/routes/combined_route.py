from flask import Blueprint, request, jsonify
import os, uuid
from services.emotion_service import detect_emotion
from services.spotify_service import get_playlist_for_mood

combined_bp = Blueprint('combined', __name__)
UPLOAD_FOLDER = 'static/temp_images'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@combined_bp.route('/predict-and-recommend', methods=['POST'])
def predict_and_recommend():
    image_file = request.files.get('image')
    if not image_file or image_file.filename == '':
        return jsonify({'error': 'No image uploaded'}), 400

    # Save image with unique name
    filename = f"{uuid.uuid4().hex}.jpg"
    filepath = os.path.join(UPLOAD_FOLDER, filename)
    image_file.save(filepath)

    try:
        # Detect mood
        mood = detect_emotion(filepath)

        # Generate playlist
        playlist_data = get_playlist_for_mood(mood)

        # Return full response
        return jsonify({
            'mood': mood.capitalize(),
            'caption': playlist_data['caption'],
            'playlist': playlist_data['songs']
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 500
