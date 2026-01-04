import React, { useState } from "react";
import axios from "axios";
import "./App.css";

function App() {
  const [longUrl, setLongUrl] = useState("");
  const [shortUrl, setShortUrl] = useState("");

  const generateShortUrl = async () => {
    try {
      const response = await axios.post("http://localhost:5000/shorten", {
        longUrl: longUrl,
      });
      setShortUrl(response.data.shortUrl);
    } catch (error) {
      alert("Backend not running or CORS error");
    }
  };

  return (
    <div className="container">
      <h2>🔗 Short URL Generator</h2>

      <input
        type="text"
        placeholder="Enter long URL"
        value={longUrl}
        onChange={(e) => setLongUrl(e.target.value)}
      />

      <button onClick={generateShortUrl}>Generate</button>

      {shortUrl && (
        <p>
          Short URL:
          <a href={shortUrl} target="_blank" rel="noreferrer">
            {shortUrl}
          </a>
        </p>
      )}
    </div>
  );
}

export default App;
