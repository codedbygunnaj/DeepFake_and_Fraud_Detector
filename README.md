🛡️ AI Sentinel: Deepfake & Fraud Detection Suite

AI Sentinel is a professional-grade, multi-modal forensic analysis suite designed to detect AI-generated media. By leveraging state-of-the-art Deep Learning architectures, the system identifies subtle artifacts in images, frequency anomalies in audio, and temporal inconsistencies in video that are invisible to the human eye.

🌟 Key Features

🎥 Video Forensic Module
Temporal Consistency Analysis: Uses a hybrid CNN-LSTM and Vision Transformer (ViT) approach to detect frame-level flickering and unnatural facial transitions.

ROI Extraction: Real-time facial landmark tracking to isolate manipulated regions.

Explainable AI (XAI): Generates heatmaps (Grad-CAM) to visualize which parts of a frame the model flagged as "synthetic."

🎙️ Audio Authenticity Analysis
Spectral Deep-Dive: Converts audio signals into Mel-Spectrograms using Librosa.

Synthetic Pattern Recognition: A custom CNN trained on the ASVspoof dataset identifies frequency gaps and "robotic" phase shifts common in text-to-speech models.

📸 Image Tamper Detection
Error Level Analysis (ELA): Identifies pixel-level manipulation by calculating compression differentials.

Metadata Forensic: Extracts EXIF data to check for AI software signatures and camera sensor consistency.

📊 Professional Dashboard
Glassmorphism UI: A sleek, high-performance interface built with React and Tailwind CSS.

Forensic Report Generation: One-click PDF export containing detailed breakdown of detection confidence, analysis methodology, and visual evidence.

🛠️ Technical Stack

Component

Technology

Frontend

React.js, Tailwind CSS, Framer Motion (Animations)

Backend

FastAPI (Python), Uvicorn

Deep Learning

PyTorch, HuggingFace Transformers, OpenCV

Data Processing

Librosa (Audio), NumPy, Pandas

Deployment

Docker, AWS/GCP (Planned)

📐 System Architecture

Ingestion: User uploads media (MP4, MP3, WAV, JPG, PNG).

Preprocessing: Normalization, frame extraction, or spectral conversion.

Inference Engine: Parallel processing via specific Forensic Agents (Video/Audio/Image).

Synthesis: Results are aggregated to determine an overall "Authenticity Score."

Reporting: Detailed metrics are displayed on the Dashboard and prepared for PDF export.

🚀 Getting Started

Prerequisites

Python 3.9+

Node.js & npm

CUDA-enabled GPU (Recommended for Video Inference)

Installation

Clone the repository:

git clone https://github.com/codedbygunnaj/deepfake_and_fraud_detector cd ai-sentinel

Backend Setup:

cd backend pip install -r requirements.txt python main.py

Frontend Setup:

cd frontend npm install npm start

🤝 Contribution & Contact

Disclaimer: AI Sentinel is a tool for forensic assistance and should be used as part of a broader verification process.
