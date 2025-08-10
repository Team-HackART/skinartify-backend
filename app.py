from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import tensorflow as tf
from PIL import Image
import numpy as np
import io
import os

os.environ["CUDA_VISIBLE_DEVICES"] = "-1"  # Disable GPU usage for compatibility

# Load model once at startup
model = tf.keras.models.load_model("skinartify_densenet_model.keras")

# Update with your actual classes in the order the model predicts
class_names = ['akiec', 'bcc', 'bkl', 'df', 'melanoma', 'nevus', 'vasc']

app = FastAPI()

# Allow requests from your Netlify site
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For testing; restrict in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"status": "Backend running", "message": "Skinartify API is live!"}

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    # Read and process the uploaded image
    image_bytes = await file.read()
    image = Image.open(io.BytesIO(image_bytes)).convert("RGB")
    image = image.resize((224, 224))  # match model input size

    # Preprocess image
    img_array = np.array(image) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    # Predict
    preds = model.predict(img_array)[0]
    result = {class_names[i]: float(preds[i]) for i in range(len(class_names))}

    return {"predictions": result}
