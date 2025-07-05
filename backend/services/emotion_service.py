import numpy as np
import cv2
from tensorflow.keras.models import load_model
from deepface.commons import functions

# Load the model from your local file — do this ONCE
emotion_model_path = "models/facial_expression_model_weights.h5"
emotion_model = load_model(emotion_model_path)

# Emotion labels used by the model
emotion_labels = ['angry', 'disgust', 'fear', 'happy', 'sad', 'surprise', 'neutral']

def detect_emotion(image_path):
    # Preprocess the image as DeepFace does
    img = functions.preprocess_face(img=image_path, target_size=(48, 48), grayscale=True, enforce_detection=False)
    
    preds = emotion_model.predict(img)[0]
    dominant_emotion = emotion_labels[np.argmax(preds)]
    
    return dominant_emotion.lower()
