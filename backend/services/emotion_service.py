from deepface import DeepFace

def detect_emotion(image_path):
    analysis = DeepFace.analyze(img_path=image_path, actions=['emotion'], enforce_detection=False)
    mood = analysis[0]['dominant_emotion'].lower()
    return mood
