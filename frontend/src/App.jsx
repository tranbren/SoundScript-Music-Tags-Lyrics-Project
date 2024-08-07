import React, { useState } from 'react';
import axios from 'axios';
import Waves from "./waves.json";
import Music from "./music.json";
import Loading from "./loading.json";
import Lottie from "lottie-react";
import './App.css'; // Import the CSS file

function App() {
  // Holds input of the submitted form
  const [artist, setArtist] = useState('');
  const [song, setSong] = useState('');
  const [tags, setTags] = useState([]);
  const [lyrics, setLyrics] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');
  const [isDataFetched, setIsDataFetched] = useState(false); // State for tracking data fetching
  const [hasSubmitted, setHasSubmitted] = useState(false); // New state for tracking form submission

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError('');
    setIsDataFetched(false); // Reset the state when new data is being fetched

    try {
      // Make POST request to Django backend
      const response = await axios.post('http://127.0.0.1:8000/api/"Place Holder"/', { artist, song });
      setTags(response.data.Tags || []); // Handle cases where Tags might be undefined

      // Parse lyrics into a list
      const lyricsData = response.data.Lyrics || '';
      const lyricsList = lyricsData.split('\n').filter(line => line.trim() !== '');
      setLyrics(lyricsList);

      // Update the state to indicate that data fetching is complete
      setIsDataFetched(true);
      setHasSubmitted(true); // Update state to indicate form has been submitted
    } catch (err) {
      console.error('Error:', err);
      setError('Error fetching tags or lyrics. Please try again.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="relative min-h-screen bg-black text-white flex flex-col items-center">
      {/* Fixed Lottie Animation at the bottom */}
      <div className="absolute bottom-0 inset-x-0 z-0">
        <Lottie animationData={Waves} loop={true} className="w-full" />
      </div>

      {/* Main content container with two columns */}
      <div
        className={`relative z-10 max-w-5xl w-[95%] sm:w-[85%] md:w-[75%] lg:w-[65%] p-6 mt-10 bg-transparent flex flex-col lg:flex-row lg:space-x-12 transition-transform duration-500 ${
          hasSubmitted ? 'lg:translate-x-0' : 'lg:translate-x-1/4'
        }`}
      >
        {/* Main content and tags column */}
        <div className="flex-1 lg:max-w-1/2">
          <div className="flex justify-center items-center space-x-4 mb-4">
            <div className="w-20">
              <Lottie animationData={Music} />
            </div>
          </div>
          <h2 className="text-2xl font-bold text-green-500 mb-4 text-center">
            Find Genres and Lyrics For Songs
          </h2>
          <form onSubmit={handleSubmit} className="space-y-4 w-full flex flex-col items-center">
            <div className="form-control w-full max-w-md">
              <label className="label">
                <span className="label-text font-semibold text-gray-300 text-xl">Artist:</span>
              </label>
              <input
                type="text"
                value={artist}
                onChange={(e) => setArtist(e.target.value)}
                className="input input-bordered w-full bg-gray-900 text-white border-green-500"
              />
            </div>
            <div className="form-control w-full max-w-md">
              <label className="label">
                <span className="label-text font-semibold text-gray-300 text-xl">Song Title:</span>
              </label>
              <input
                type="text"
                value={song}
                onChange={(e) => setSong(e.target.value)}
                className="input input-bordered w-full bg-gray-900 text-white border-green-500"
              />
            </div>
            <button
              type="submit"
              disabled={loading}
              className={`btn w-full max-w-md flex items-center justify-center text-lg ${
                loading ? 'bg-black border-transparent' : 'bg-green-500 hover:bg-green-600 border-green-600'
              } text-white outline-none`}
            >
              {loading ? (
                <Lottie animationData={Loading} className="w-50 h-10" />
              ) : (
                'Submit'
              )}
            </button>
          </form>
          {error && <p className="text-red-500 mt-4 text-center">{error}</p>}
          {tags.length > 0 && (
            <div className="mt-6">
              <h2 className="text-2xl font-semibold text-green-500 text-center mb-5">Tags:</h2>
              <div className="flex flex-wrap justify-center gap-4">
                {tags.map((tag, index) => (
                  <span
                    key={index}
                    className="bg-black text-green-500 px-4 py-2 rounded-full border border-green-500 transition-transform transform hover:scale-105 hover:bg-green-600 hover:text-white"
                  >
                    {tag}
                  </span>
                ))}
              </div>
            </div>
          )}
        </div>

        {/* Lyrics column */}
        <div className="flex-1 lg:max-w-1/2 mt-6 lg:mt-0">
          {lyrics.length > 0 && (
            <div className="lyrics-container">
            <h2 className="lyrics-title">Lyrics:</h2>
            <div className="lyrics-content">
              <ul className="lyrics-list">
                {lyrics.map((line, index) => (
                  <li key={index} className="lyrics-list-item">{line}</li>
                ))}
              </ul>
            </div>
          </div>
          )}
        </div>
      </div>
    </div>
  );
}

export default App;
