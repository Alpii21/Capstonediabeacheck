DiabeaCheck Backend API MLProyek ini bertujuan untuk mengembangkan model machine learning berbasis TensorFlow dan Keras untuk memprediksi risiko diabetes berdasarkan parameter fisiologis. Model ini menggunakan Multilayer Perceptron (MLP) yang telah dilatih dan diintegrasikan dengan FastAPI untuk menyediakan endpoint prediksi.Fitur UtamaModel Klasifikasi Diabetes:Memprediksi kemungkinan seseorang menderita diabetes berdasarkan input data seperti Age, BMI, Glucose, Insulin, dan BloodPressure.Menggunakan model MLP yang telah dilatih sebelumnya.Preprocessing Data Otomatis:Melakukan penskalaan data input menggunakan StandardScaler yang telah dilatih sebelumnya untuk memastikan performa model yang optimal.Endpoint API Sederhana:Menyediakan endpoint /predict/ yang mudah digunakan untuk integrasi dengan aplikasi frontend atau layanan lainnya.Informasi Model dan DataModel ini dilatih menggunakan dataset yang relevan untuk prediksi diabetes, dengan fitur-fitur seperti Usia, BMI, Glukosa, Insulin, dan Tekanan Darah. Detail lebih lanjut tentang proses pelatihan dapat ditemukan di Jupyter Notebook capstone_diabeacheck.ipynb.Struktur BerkasDiabeaCheck/
├── app.py
├── model_artifacts/
│   ├── diabetes_mlp_model.h5
│   └── scaler.joblib
├── capstone_diabeacheck.ipynb
├── inference.ipynb
└── requirements.txt
app.py: Aplikasi utama FastAPI yang menangani loading model dan endpoint prediksi.model_artifacts/: Direktori yang berisi artefak model dan scaler yang telah dilatih.diabetes_mlp_model.h5: Model MLP yang telah dilatih (TensorFlow/Keras).scaler.joblib: Objek StandardScaler yang telah dilatih untuk penskalaan data.capstone_diabeacheck.ipynb: Jupyter Notebook yang digunakan untuk melatih dan mengevaluasi model.inference.ipynb: Jupyter Notebook yang mendemonstrasikan cara melakukan inferensi dengan model yang telah dilatih secara lokal.requirements.txt: Daftar dependensi Python yang diperlukan.Langkah-langkah InstalasiKompatibilitas Python: Pastikan Python >= 3.8Clone repositori ini:git clone https://github.com/Alpii21/Capstonediabeacheck.git
cd Capstonediabeacheck/DiabeaCheck # Navigasi ke direktori proyek
Instal dependensi:pip install -r requirements.txt
Jalankan notebook (opsional, untuk melihat proses pelatihan atau inferensi lokal):jupyter notebook capstone_diabeacheck.ipynb
ataujupyter notebook inference.ipynb
PenggunaanMenjalankan Aplikasi API:Mulai server FastAPI menggunakan Uvicorn:uvicorn app:app --host 0.0.0.0 --port 8000
Aplikasi akan tersedia di http://your-ip:8000.Menggunakan Endpoint API (POST /predict/):Deskripsi: Memprediksi risiko diabetes berdasarkan parameter input yang diberikan.Contoh Request Body:{
  "Age": 45,
  "BMI": 28.5,
  "Glucose": 120.0,
  "Insulin": 50.0,
  "BloodPressure": 80
}
Contoh Response Sukses:{
  "prediction": 0,
  "probability": 0.12345,
  "label": "Tidak Diabetes"
}
atau{
  "prediction": 1,
  "probability": 0.87654,
  "label": "Diabetes"
}
Penanganan Kesalahan: Mengembalikan pesan kesalahan (HTTP 500) jika artefak model tidak ditemukan atau (HTTP 422) jika input tidak valid.Cara KerjaPrediksi DiabetesData input (Age, BMI, Glucose, Insulin, BloodPressure) diterima melalui endpoint POST /predict/.Data input diskalakan menggunakan scaler.joblib yang telah dimuat saat aplikasi startup.Data yang sudah diskalakan kemudian diberikan ke diabetes_mlp_model.h5 untuk mendapatkan probabilitas prediksi.Probabilitas tersebut dikonversi menjadi label biner (0 untuk "Tidak Diabetes" atau 1 untuk "Diabetes") berdasarkan ambang batas 0.5, dan juga menyediakan label teks ("Diabetes" atau "Tidak Diabetes").DependensiProyek ini menggunakan dependensi berikut, yang tercantum dalam requirements.txt:fastapi>=0.103.0
pydantic>=2.0.0
joblib>=1.3.0
numpy>=1.26.0
tensorflow>=2.10.0
pandas>=2.0.0
scikit-learn>=1.3.0
matplotlib>=3.8.0
seaborn>=0.13.0
imblearn>=0.11.0
uvicorn>=0.23.0
Instal semua dependensi menggunakan:pip install -r requirements.txt
KontributorProyek ini dikembangkan oleh:[Nama Anda/Tim Anda] | Machine Learning Engineer
