
import React from 'react';
import { Link } from 'react-router-dom';

function Navbar() {
  const navbarStyle = {
    backgroundColor: '#1e1e2f',
    padding: '15px 30px',
    display: 'flex',
    justifyContent: 'space-between',
    alignItems: 'center',
    color: 'white',
    fontFamily: 'sans-serif',
    boxShadow: '0 2px 10px rgba(0, 0, 0, 0.1)'
  };

  const linkStyle = {
    color: 'white',
    marginLeft: '20px',
    textDecoration: 'none',
    fontSize: '16px'
  };

  return (
    <nav style={navbarStyle}>
      <h3 style={{ margin: 0 }}>🎵 Moodify</h3>
      <div>
        <Link to="/" style={linkStyle}>Home</Link>
        <Link to="/about" style={linkStyle}>About</Link>
      </div>
    </nav>
  );
}

export default Navbar;
