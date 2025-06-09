# DiabeaCheck Multi Layer Perceptron

Proyek ini menggunakan dataset diabetes dari Pima Indians dan NHANES untuk membangun model prediksi menggunakan Neural Network (MLP) dengan TensorFlow/Keras. Data di-preprocess dengan standardisasi dan penyeimbangan kelas menggunakan SMOTE.

## Fitur Utama

* Preprocessing data (scaling dan balancing)
* Neural Network model (MLP)
* Evaluasi model dengan classification report dan confusion matrix
* Menyimpan model terlatih dalam format `.h5`

## Struktur File

* `deteksi_diabetes.ipynb`: Notebook utama yang memuat seluruh proses dari preprocessing hingga pelatihan dan evaluasi model.
* `diabetes.csv dan NHANES_age_prediction.csv`: Dataset yang digunakan (pastikan file ini tersedia di direktori kerja).
* `diabetes_mlp_model.h5`: Model hasil pelatihan.

## Instalasi dan Persiapan

Pastikan environment Anda sudah memiliki dependensi berikut:

```bash
pip install pandas numpy matplotlib seaborn scikit-learn imbalanced-learn tensorflow
```

## Menjalankan Notebook

1. Pastikan file `diabetes.csv` berada dalam folder yang sama dengan notebook.
2. Jalankan semua sel di `deteksi_diabetes.ipynb`.
3. Model akan disimpan sebagai `model_diabetes.h5`.

## Output Model

* Akurasi evaluasi model pada data uji.
* Classification report: precision, recall, f1-score.
* Confusion matrix.

## Catatan Tambahan

* Model menggunakan EarlyStopping untuk mencegah overfitting.
* Teknik SMOTE digunakan agar distribusi kelas menjadi seimbang.

---

**Author:** *Diisi oleh nama Anda*
**Dataset:** Pima Indians Diabetes Dataset
