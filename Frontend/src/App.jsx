import React, { useState } from "react";
import "./index.css";

function WebSiteBuilder() {
  const [file, setFile] = useState(null);
  const [preview, setPreview] = useState(null);
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  // Handle file selection
  const handleFileChange = (e) => {
    const selectedFile = e.target.files[0];
    if (!selectedFile) return;

    setFile(selectedFile);
    setPreview(URL.createObjectURL(selectedFile));
    setResult(null);
  };

  // Handle upload to backend
  const handleUpload = async () => {
    if (!file) {
      alert("Please select a file first");
      return;
    }

    const formData = new FormData();
    formData.append("file", file);

    try {
      setLoading(true);

      const response = await fetch(`${import.meta.env.VITE_API_URL}predict`, {
        method: "POST",
        body: formData,
      });

      const data = await response.json();
      setResult(data);

    } catch (error) {
      alert("Error connecting to backend");
      console.error(error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="container">
      <h1>AI Deepfake Detector</h1>

      <input
        type="file"
        accept="image/*,video/*"
        onChange={handleFileChange}
      />

      {preview && (
        <div className="preview">
          {file.type.startsWith("image") ? (
            <img src={preview} alt="Preview" />
          ) : (
            <video src={preview} controls />
          )}
        </div>
      )}

      <button onClick={handleUpload}>
        {loading ? "Analyzing..." : "Predict"}
      </button>

      {result && (
        <div className="result">
          <h2>
            Prediction:{" "}
            <span
              style={{
                color:
                  result.prediction === "Real" ? "lightgreen" : "red",
              }}
            >
              {result.prediction}
            </span>
          </h2>

          <p>
            Confidence: {(result.confidence * 100).toFixed(2)}%
          </p>
        </div>
      )}
    </div>
  );
}

export { WebSiteBuilder };