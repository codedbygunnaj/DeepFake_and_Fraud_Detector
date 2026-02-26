from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import shutil

from transformers import pipeline
from PIL import Image

app = FastAPI()

classifier = pipeline(
    "image-classification",
    model="dima806/deepfake_vs_real_image_detection"
)

# CORS enable (React ko allow karega)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/predict")
async def predict(file: UploadFile = File(...)):

    image = Image.open(file.file).convert("RGB")

    result = classifier(image)

    label = result[0]['label']
    score = result[0]['score']

    return {
        "prediction": label,
        "confidence": float(score)
    }


# uvicorn main:app --reload