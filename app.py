# app.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import numpy as np
import pandas as pd
import os

# Definisikan path ke artefak model
MODEL_DIR = 'model_artifacts'
MODEL_PATH = os.path.join(MODEL_DIR, 'best_random_forest_model_rfe.pkl')
SCALER_PATH = os.path.join(MODEL_DIR, 'scaler.pkl')
RFE_SELECTOR_PATH = os.path.join(MODEL_DIR, 'rfe_selector.pkl')

# Muat model, scaler, dan RFE selector saat aplikasi dimulai
try:
    model = joblib.load(MODEL_PATH)
    scaler = joblib.load(SCALER_PATH)
    rfe_selector = joblib.load(RFE_SELECTOR_PATH)
    print("Model, Scaler, dan RFE Selector berhasil dimuat.")
except FileNotFoundError as e:
    print(f"Error: File artefak model tidak ditemukan. Pastikan Anda sudah menjalankan bagian penyimpanan model. Detail: {e}")
    model = None
    scaler = None
    rfe_selector = None

# Inisialisasi aplikasi FastAPI
app = FastAPI()

class PredictionInput(BaseModel):
    Pregnancies: float
    Glucose: float
    BloodPressure: float
    SkinThickness: float
    Insulin: float
    BMI: float
    DiabetesPedigreeFunction: float
    Age: float

# Mendefinisikan endpoint prediksi
@app.post("/predict/")
async def predict_diabetes(data: PredictionInput):
    if model is None or scaler is None or rfe_selector is None:
        raise HTTPException(status_code=500, detail="Model atau artefak lainnya gagal dimuat saat startup.")

    input_data_np = np.array([
        data.Pregnancies,
        data.Glucose,
        data.BloodPressure,
        data.SkinThickness,
        data.Insulin,
        data.BMI,
        data.DiabetesPedigreeFunction,
        data.Age
    ]).reshape(1, -1)

    # Feature scaling menggunakan scaler yang sudah dimuat
    input_data_scaled = scaler.transform(input_data_np)

    # Feature selection menggunakan RFE selector yang sudah dimuat
    input_data_rfe = rfe_selector.transform(input_data_scaled)

    # Prediksi menggunakan model yang sudah dimuat
    prediction = model.predict(input_data_rfe)

    # Konversi hasil prediksi (numpy array) ke tipe data Python native
    result = int(prediction[0])

    # Interpretasikan hasil prediksi
    prediction_label = "Diabetes" if result == 1 else "Tidak Diabetes"

    # Kembalikan hasil prediksi dalam format JSON
    return {"prediction": prediction_label, "raw_output": result}

@app.get("/")
async def read_root():
    return {"message": "API Deteksi Diabetes Berjalan"}


