from deepface import DeepFace

def detect_emotion(image_path):
    try:
        result = DeepFace.analyze(img_path=image_path, actions=["emotion"], enforce_detection=False)
        mood = result[0]["dominant_emotion"].lower()
        return mood
    except Exception as e:
        return f"Error: {str(e)}"
