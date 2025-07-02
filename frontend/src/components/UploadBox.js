import React, { useState, useRef, useCallback } from 'react';
import Webcam from 'react-webcam';

function UploadBox({ onImageSelect }) {
  const [previewUrl, setPreviewUrl] = useState(null);
  const [isCameraOpen, setIsCameraOpen] = useState(false);
  const webcamRef = useRef(null);
  const fileInputRef = useRef(null);

  const handleFileChange = (e) => {
    const file = e.target.files[0];
    if (file) {
      const url = URL.createObjectURL(file);
      setPreviewUrl(url);
      onImageSelect(file);

      // ✅ Important fix: allow re-uploading same file
      e.target.value = ''; // <-- this line is crucial
    }
  };

  const handleCapture = useCallback(() => {
    const imageSrc = webcamRef.current.getScreenshot();
    setPreviewUrl(imageSrc);

    // Convert data URL to Blob
    fetch(imageSrc)
      .then(res => res.blob())
      .then(blob => {
        const file = new File([blob], 'captured.jpg', { type: 'image/jpeg' });
        onImageSelect(file);
      });

    setIsCameraOpen(false);
  }, [webcamRef]);

  return (
    <div>
      <h5 className="mb-3 fw-semibold">📸 Upload or Take a Selfie</h5>

      <div className="d-flex gap-2 mb-3">
        <button
          className="btn btn-outline-primary"
          onClick={() => fileInputRef.current.click()}
        >
          📤 Upload from Gallery
        </button>

        <button
          className="btn btn-outline-success"
          onClick={() => setIsCameraOpen(true)}
        >
          📷 Take a Photo
        </button>
      </div>

      {/* Hidden file input */}
      <input
        type="file"
        accept="image/*"
        ref={fileInputRef}
        style={{ display: 'none' }}
        onChange={handleFileChange}
      />

      {/* Webcam modal */}
      {isCameraOpen && (
        <div className="mb-3 text-center">
          <Webcam
            audio={false}
            ref={webcamRef}
            screenshotFormat="image/jpeg"
            videoConstraints={{ facingMode: 'user' }}
            className="rounded shadow-sm"
            style={{ width: '100%', maxWidth: '300px' }}
          />
          <div className="mt-2">
            <button className="btn btn-success me-2" onClick={handleCapture}>
              📸 Capture
            </button>
            <button className="btn btn-secondary" onClick={() => setIsCameraOpen(false)}>
              ❌ Cancel
            </button>
          </div>
        </div>
      )}

      {/* Preview */}
      {previewUrl && !isCameraOpen && (
        <div>
          <img
            src={previewUrl}
            alt="Preview"
            className="img-fluid rounded shadow-sm"
          />
        </div>
      )}
    </div>
  );
}

export default UploadBox;
