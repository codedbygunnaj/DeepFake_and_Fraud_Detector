from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import shutil

app = FastAPI()

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

    with open(file.filename, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {
        "prediction": "Fake",
        "confidence": 0.87
    }


# uvicorn main:app --reload