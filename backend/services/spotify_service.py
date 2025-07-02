import os
from dotenv import load_dotenv
import requests
import base64
import random

load_dotenv()
CLIENT_ID = os.getenv('SPOTIFY_CLIENT_ID')
CLIENT_SECRET = os.getenv('SPOTIFY_CLIENT_SECRET')

# ✅ Bollywood style genre-based mappings for all moods
mood_to_genres = {
    'happy': [
        'bollywood dance', 'party hindi', 'bollywood upbeat', 'hindi celebration'
    ],
    'sad': [
        'arijit singh sad', 'sad hindi', 'emotional bollywood', 'bollywood heartbreak'
    ],
    'angry': [
        'bollywood revenge', 'hindi action', 'bollywood rage', 'indian rap'
    ],
    'fear': [
        'bollywood thriller', 'hindi horror soundtrack', 'dark suspense india', 'cinematic fear hindi'
    ],
    'surprise': [
        'quirky bollywood', 'fusion hindi', 'genre blend india', 'unexpected bollywood'
    ],
    'disgust': [
        'healing hindi', 'bollywood detox', 'meditative india', 'calm instrumental hindi'
    ],
    'neutral': [
        'bollywood chill', 'hindi lofi', 'relaxing india', 'bollywood smooth'
    ]
}

mood_captions = {
    'happy': "You're glowing with joy! Here's something to keep the celebration going 🎉🩰 This playlist will help you vibe with your current mood.",
    'sad': "Had a heartbreak? Feeling heavy? Here’s your soulful sad mix to cry it out 😢💔 Let the music vibe with your feelings.",
    'angry': "You're fired up and ready to roar! Let this fierce Bollywood mix match your mood 💥🔥 Whether it's rage or rebellion — here's your sonic revenge.",
    'fear': "Feeling scared or anxious? Here’s an eerie cinematic soundscape to vibe with the tension 👻",
    'surprise': "Whoa! Didn’t expect that? This experimental mix matches your surprise vibe 😲🎊",
    'neutral': "You’re in the middle zone. These smooth, mellow tunes will help you stay centered ☕",
    'disgust': "Need to clear your mind? Let these minimal and ambient sounds help you vibe through it 🧘‍♀️"
}

def get_spotify_token():
    url = 'https://accounts.spotify.com/api/token'
    auth_header = base64.b64encode(f"{CLIENT_ID}:{CLIENT_SECRET}".encode()).decode()

    headers = {
        'Authorization': f'Basic {auth_header}',
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    data = {'grant_type': 'client_credentials'}

    response = requests.post(url, headers=headers, data=data)
    response.raise_for_status()
    return response.json()['access_token']


def get_playlist_for_mood(mood):
    mood = mood.lower()
    token = get_spotify_token()
    headers = {'Authorization': f'Bearer {token}'}
    songs = []

    try:
        queries = mood_to_genres.get(mood, ['bollywood'])
        seen_urls = set()

        for query in queries:
            params = {
                'q': query,
                'type': 'track',
                'limit': 10,
                'offset': random.randint(0, 40),
                'market': 'IN'
            }

            res = requests.get('https://api.spotify.com/v1/search', headers=headers, params=params)
            res.raise_for_status()
            items = res.json().get('tracks', {}).get('items', [])

            for track in items:
                if not track or not track.get('album') or not track.get('external_urls'):
                    continue
                url = track['external_urls']['spotify']

                # ✅ Occasionally allow repeats across sessions; skip only in this loop
                if url in seen_urls:
                    continue
                seen_urls.add(url)

                songs.append({
                    'name': track['name'],
                    'image': track['album']['images'][0]['url'],
                    'spotify_url': url
                })
                if len(songs) >= 10:
                    break

            if len(songs) >= 10:
                break

        return {
            'caption': mood_captions.get(mood, "Here's a playlist to match your vibe."),
            'songs': songs[:10]
        }

    except Exception as e:
        print(f"[ERROR] Playlist generation failed: {e}")
        return {
            'caption': "Oops! Something went wrong while fetching your songs.",
            'songs': []
        }
