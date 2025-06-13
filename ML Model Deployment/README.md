# DiabeaCheck Multi Layer Perceptron dan Integrasi API ML

![Python](https://img.shields.io/badge/python-v3.8+-blue.svg)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.10+-orange.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.103+-green.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

Sistem Prediksi Risiko Diabetes berbasis Machine Learning (MLP) yang di-deploy menggunakan FastAPI dan Docker. Proyek ini bertujuan untuk memberikan deteksi dini terhadap potensi diabetes berdasarkan data input kesehatan pengguna seperti usia, BMI, kadar glukosa, dan lainnya.

---

## 📉 Fitur Utama

* Prediksi risiko diabetes dengan model **Multilayer Perceptron (MLP)** berbasis TensorFlow
* API dibangun dengan **FastAPI**
* Dockerized untuk kemudahan deployment
* Validasi input menggunakan **Pydantic**
* Dukungan log dan error handling

---

## 🛋️ Arsitektur Model ML

```
model_artifacts/
├── diabetes_mlp_model.h5       # Model MLP hasil training
├── scaler.joblib               # Scaler (MinMax atau Standard)
```

Model dan scaler diload saat server API dijalankan. Jika file tidak ditemukan, API akan menampilkan error saat health check atau prediksi.

---

## 📄 Struktur Proyek

```
.
├── app.py                      # Main FastAPI App
├── requirements.txt            # Dependensi Python
├── Dockerfile                  # Docker Build Config
├── .dockerignore               # File yang diabaikan saat build Docker
├── model_artifacts/            # Folder untuk model dan scaler
└── README.md                   # Dokumentasi proyek ini
```

---

## 🚀 Menjalankan Proyek Secara Lokal

### 1. Clone Repo

```bash
git clone https://github.com/Alpii21/Capstonediabeacheck.git
cd Capstonediabeacheck
```

### 2. Buat & Aktifkan Virtual Env

```bash
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows
```

### 3. Install Dependensi

```bash
pip install -r requirements.txt
```

### 4. Jalankan Aplikasi

```bash
uvicorn app:app --reload
```

---

## 🛠️ Menjalankan dengan Docker

### Build Image

```bash
docker build -t diabeacheck-api .
```

### Run Container

```bash
docker run -d -p 8000:8000 diabeacheck-api
```

---

## 📍 Endpoint API

### 1. Health Check

```
GET /health
```

Respon:

```json
{
  "status": "ok",
  "message": "Model dan Scaler tersedia"
}
```

### 2. Prediksi

```
POST /predict
```

Contoh input JSON:

```json
{
  "Age": 35,
  "BMI": 26.5,
  "Glucose": 140.2,
  "Insulin": 80.0,
  "BloodPressure": 72
}
```

Contoh output:

```json
{
  "prediction": "Diabetes",
  "raw_output": 1,
  "probability_percent": "76.45%"
}
```

---

## 📁 Dependensi

* fastapi
* uvicorn
* numpy==1.23.5
* joblib
* tensorflow-cpu==2.10.0
* scikit-learn

---

## 🛡️ Keamanan & Validasi

* Validasi input dilakukan menggunakan `pydantic`
* Logging setiap input dan hasil prediksi
* Error handling di semua proses utama

---

## 👍 Kontribusi

Kami menyambut kontribusi dari komunitas! Untuk berkontribusi:

### Guidelines

* Fork repository ini
* Buat branch baru (`git checkout -b feature/AmazingFeature`)
* Commit perubahan (`git commit -m 'Add some AmazingFeature'`)
* Push ke branch (`git push origin feature/AmazingFeature`)
* Buat Pull Request

### Area Kontribusi

* Model Improvement: Optimasi akurasi dan performa model
* API Enhancement: Penambahan fitur dan endpoint baru
* Documentation: Perbaikan dan penambahan dokumentasi
* Testing: Penambahan unit tests dan integration tests
* Performance: Optimasi kecepatan inference dan memory usage

### Code Standards

* Gunakan PEP 8
* Sertakan docstrings dan type hints
* Tangani error dengan baik

---

## 👥 Tim Pengembang

### 🔎 Machine Learning Team

* Alfiah (MC796D5X0076) – Politeknik Baja Tegal
* Elaine Agustina (MC834D5X1658) – Universitas Pelita Harapan
* Rafly Ashraffi Rachmat (MC796D5Y0101) – Politeknik Baja Tegal

---

## 📄 Lisensi

Proyek ini dilisensikan di bawah MIT License.

```
MIT License

Copyright (c) 2025 DiabeaCheck Team

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
... (pemotongan lisensi untuk ringkasan) ...
```

---
