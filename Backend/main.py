from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from transformers import pipeline
from PIL import Image
from facenet_pytorch import MTCNN
import cv2
import numpy as np

app = FastAPI()

# CORS enable
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Face detector
mtcnn = MTCNN(keep_all=False)

# Deepfake detection model (ViT based)
classifier = pipeline(
    "image-classification",
    model="prithivMLmods/DeepFake-Detection-Model"
)

@app.post("/predict")
async def predict(file: UploadFile = File(...)):

    # Convert uploaded image to PIL
    image = Image.open(file.file).convert("RGB")

    # Detect face
    boxes, _ = mtcnn.detect(image)

    if boxes is None:
        return {
            "prediction": "No Face Detected",
            "confidence": 0.0
        }

    # Crop first face
    x1, y1, x2, y2 = map(int, boxes[0])
    face = image.crop((x1, y1, x2, y2))

    # Run deepfake model on face
    result = classifier(face)

    score = result[0]['score']

    # Threshold logic
    if score > 0.75:
        prediction = "Fake"
    elif score < 0.35:
        prediction = "Real"
    else:
        prediction = "Uncertain"

    return {
        "prediction": prediction,
        "confidence": float(score)
    }
# uvicorn main:app --reload