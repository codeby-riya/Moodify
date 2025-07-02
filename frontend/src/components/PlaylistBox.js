
import React from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';

function PlaylistBox({ playlistData }) {
  if (!playlistData || !playlistData.playlist || playlistData.playlist.length === 0) {
    return (
      <div className="text-center text-muted">
        <h4 className="fw-bold mb-3">🎧 Your Mood-Based Playlist</h4>
        <p>Please upload a selfie and we'll generate the perfect playlist for you!</p>
      </div>
    );
  }

  return (
    <div>
      <h4 className="fw-bold mb-4 text-center">🎧 Your Mood-Based Playlist</h4>

      {/* Optional: Mood + Caption */}
      <div className="mb-4 text-center">
        <p className="fs-5"><strong>Mood:</strong> {playlistData.mood}</p>
        <p className="fst-italic">{playlistData.caption}</p>
      </div>

      {/* Playlist */}
      <div className="row row-cols-1 row-cols-md-2 g-4">
        {playlistData.playlist.map((song, index) => (
          <div key={index} className="col">
            <div className="card h-100 shadow-sm border-0">
              <img src={song.image} className="card-img-top" alt={song.name} />
              <div className="card-body">
                <h5 className="card-title">{song.name}</h5>
                <div className="ratio ratio-16x9">
                  <iframe
                    src={`https://open.spotify.com/embed/track/${extractSpotifyTrackId(song.spotify_url)}`}
                    width="100%"
                    height="80"
                    frameBorder="0"
                    allowtransparency="true"
                    allow="encrypted-media"
                    title={song.name}
                  ></iframe>
                </div>
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}

// Helper to extract track ID from URL
function extractSpotifyTrackId(url) {
  const parts = url.split('/track/');
  return parts.length > 1 ? parts[1].split('?')[0] : '';
}

export default PlaylistBox;
