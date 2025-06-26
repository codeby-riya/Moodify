# Moodify

Moodify is a web app that recommends music based on the user's mood. The user uploads a photo, and the system tries to predict their emotion using a machine learning model. Based on the predicted mood, the app fetches a playlist using the Spotify API.

This was a project I built to explore how emotion recognition and music recommendation can work together.

---

## Features

- Upload your image to detect your mood
- Get a playlist that matches how you're feeling
- Frontend built using React
- Backend with Flask and Python
- Uses Spotify API for music data
- Simple and responsive UI

---

## Tech Stack

- **Frontend:** React, HTML/CSS
- **Backend:** Flask (Python)
- **ML Model:** Trained using Python libraries (like OpenCV, Keras, etc.)
- **Music API:** Spotify Web API

---

## How it Works (Short Overview)

1. User uploads a photo from the browser.
2. The photo is sent to the backend (Flask server).
3. A pre-trained model predicts the emotion (like happy, sad, angry, etc.).
4. Based on the result, the server queries the Spotify API for songs related to that mood.
5. The frontend receives the playlist and displays it to the user.

---


## Notes

This project was built as a personal experiment, and I plan to improve it further by:
- Making the emotion model more accurate
- Adding better UI styling
- Possibly supporting audio-based mood detection
