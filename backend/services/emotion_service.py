from deepface import DeepFace
from deepface.basemodels import Emotion
from keras.models import load_model
import os

# Load the Emotion model architecture
emotion_model = Emotion.loadModel()

# Load pre-downloaded weights from local file
model_path = os.path.join("models", "facial_expression_model_weights.h5")
emotion_model.load_weights(model_path)

# Function to predict emotion using the local model
def detect_emotion(image_path):
    analysis = DeepFace.analyze(
        img_path=image_path,
        actions=['emotion'],
        enforce_detection=False,
        models={"emotion": emotion_model}  # Use our locally loaded model
    )
    mood = analysis[0]['dominant_emotion'].lower()
    return mood
