<div align="center">

# ⚙️ SkinARTify - Backend API

**The backend server and machine learning API for the SkinARTify skin lesion classification project.**

</div>

This repository provides a comprehensive overview of the backend service powering the **SkinARTify Web App**. The backend is responsible for processing image uploads, running inference with a deep learning model, and returning classification results.

> **Note**: This GitHub repository is for demonstration and documentation purposes. The complete, up-to-date source code is actively developed and deployed on Hugging Face Spaces.

---

## 🚀 Live API & Source Code

The fully functional API and the source code are hosted together in a single Hugging Face Space.

-   **Live API Endpoint & Source Code:** **[Hugging Face Space](https://huggingface.co/spaces/aryan195a/SKINARTIFY_backend)**

---

## 🛠️ Technology Stack

| Component          | Technology                 | Description                                                      |
| :----------------- | :------------------------- | :--------------------------------------------------------------- |
| **API Server** | Node.js, Express           | Handles HTTP requests, file uploads, and API routing.            |
| **Machine Learning** | Python, Keras (TensorFlow) | Runs the prediction script and performs inference with the model. |
| **Deployment** | Hugging Face Spaces        | A platform for hosting the backend API and the ML model.         |

---

## 🏗️ Architecture Overview

The backend uses a hybrid approach to leverage the strengths of both Node.js and Python:

1.  **Node.js/Express Server**: The primary server receives `multipart/form-data` image uploads from the frontend. It handles request validation and temporarily saves the uploaded image.
2.  **Python Script Invocation**: To avoid blocking the Node.js event loop with heavy computation, the Express server invokes a separate Python script as a child process, passing the path of the saved image.
3.  **Model Inference**: The Python script loads the fine-tuned DenseNet121 model, preprocesses the image, and performs the classification.
4.  **JSON Response**: The prediction results (a list of lesion types and their confidence scores) are passed back to the Node.js server, which then formats and sends the final JSON response to the client.

---

## 🧠 Model & API Details

### **API Endpoints**

| Method | Endpoint      | Description                                                          |
| :----- | :------------ | :------------------------------------------------------------------- |
| `GET`  | `/api/health` | Health check to confirm if the server is running.                    |
| `POST` | `/api/predict`| Upload an image for prediction. Expects `multipart/form-data` with an `image` field. |

### **Model Requirements**

-   **Input Shape**: `(224, 224, 3)`
-   **Output Classes**: 7 classes, with the following order:
    -   `akiec` (Actinic keratoses)
    -   `bcc` (Basal cell carcinoma)
    -   `bkl` (Benign keratosis-like lesions)
    -   `df` (Dermatofibroma)
    -   `melanoma` (Melanoma)
    -   `nevus` (Melanocytic nevi)
    -   `vasc` (Vascular lesions)

---

## ⚠️ Medical Disclaimer

This API is part of an application designed for **educational and research purposes only**. The predictions are not a substitute for professional medical diagnosis. Always consult a qualified healthcare professional for any medical concerns or advice.
