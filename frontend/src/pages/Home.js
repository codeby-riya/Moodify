import React, { useState, useEffect } from 'react';
import Introduction from '../components/Introduction';
import UploadBox from '../components/UploadBox';
import PlaylistBox from '../components/PlaylistBox';
import 'bootstrap/dist/css/bootstrap.min.css';

function Home() {
  const [image, setImage] = useState(null);
  const [playlistData, setPlaylistData] = useState(null); // will store mood + playlist

  useEffect(() => {
    if (!image) return;

    const uploadImage = async () => {
      const formData = new FormData();
      formData.append('image', image);

      try {
        const res = await fetch('http://127.0.0.1:5000/predict-and-recommend', {
          method: 'POST',
          body: formData
        });
        const data = await res.json()
        console.log('Received from backend:', data);
        setPlaylistData(data);
      } catch (err) {
        console.error('Error uploading image:', err);
      }
    };

    uploadImage();
  }, [image]);

  return (
    <div className="container my-5">
      <div className="row gx-4 gy-4">
        {/* Left Sidebar: Introduction + Upload */}
        <div className="col-md-4">
          <div className="bg-warning-subtle p-4 rounded shadow-sm mb-4">
            <Introduction />
          </div>
          <div className="bg-info-subtle p-4 rounded shadow-sm">
            <UploadBox onImageSelect={setImage} />
          </div>
        </div>

        {/* Right Panel: Playlist */}
        <div className="col-md-8">
          <div className="bg-light p-5 rounded shadow-sm">
            <PlaylistBox image={image} playlistData={playlistData} />
          </div>
        </div>
      </div>
    </div>
  );
}

export default Home;
