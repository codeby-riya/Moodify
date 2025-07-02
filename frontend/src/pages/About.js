import React from 'react';

function About() {
  return (
    <div className="container py-5">
      <div className="bg-light p-5 rounded shadow">
        <h2 className="text-center mb-4 text-primary">Let Your Mood Play the Music 🎧</h2>

        <p className="lead text-center mb-4">
          Welcome to <strong>Moodify</strong>, where your emotions create the soundtrack of your life.
        </p>

        <p className="mb-3">
          We believe music is more than just sound — it's a reflection of your feelings, your energy, and your story in the moment.
          With cutting-edge AI and the power of deep learning, Moodify analyzes your selfie to understand your current mood and
          instantly curates a personalized playlist that fits your vibe.
        </p>

        <p className="mb-4">
          Whether you're feeling joyful, reflective, calm, or a bit blue — Moodify is here to tune in to your emotions and turn them into melodies.
        </p>

        <h4 className="text-success mb-3">What We Offer:</h4>
        <ul className="list-group list-group-flush mb-4">
          <li className="list-group-item"> AI-powered mood detection from selfies</li>
          <li className="list-group-item"> Curated playlists using the Spotify API</li>
          <li className="list-group-item"> Seamless mood-based music experience</li>
          <li className="list-group-item"> A simple and beautiful interface</li>
        </ul>

        <p className="text-center fs-5">
          So go ahead — upload your selfie and let Moodify be your personal DJ. <br />
          <strong>Because your feelings deserve to be heard.</strong>
        </p>
      </div>
    </div>
  );
}

export default About;
