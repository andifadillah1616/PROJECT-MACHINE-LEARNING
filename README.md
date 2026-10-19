# Prediksi Kemenangan PUBG Mobile

Project ini mengolah dataset PUBG Mobile untuk melihat pola statistik permainan dan membuat model prediksi pada kolom `Win`.

## Dataset

- **Nama:** PUBG Mobile
- **Sumber:** Kaggle
- **Link:** https://www.kaggle.com/datasets/aliiihussain/pubg-mobile-win-and-performance-prediction-dataset
- **Data yang dipakai:** 2.500 baris dan 16 kolom
- **Target:** `Win` (0 = tidak menang, 1 = menang)
- **Pembagian data:** 80% train dan 20% test (`random_state=42`)

## Tahapan

1. Data loading
2. Data cleaning
3. EDA dan visualisasi
4. EXDA untuk melihat hubungan antarvariabel
5. Pembagian data training dan testing
6. Modeling
7. Evaluasi model

## Target dan model

Kolom `Win` digunakan sebagai target:
- `0` = tidak menang
- `1` = menang

Karena target memiliki dua kelas, project ini menggunakan klasifikasi dengan **Gradient Boosting Classifier (GBC)**.

## Evaluasi

Metrik utama:
- Accuracy
- Precision
- Recall
- F1-score
- Confusion Matrix

MAE, MSE, dan R² bisa ditampilkan sebagai informasi tambahan, tetapi bukan metrik utama untuk klasifikasi.

## Cara menjalankan

1. Buka folder project di VS Code.
2. Pastikan Python dan Jupyter tersedia.
3. Install library jika belum ada:

   ```bash
   pip install pandas matplotlib seaborn scikit-learn jupyter
   ```

4. Buka `PUBG_Mobile_Fadil.ipynb`.
5. Jalankan setiap cell dari atas ke bawah.
