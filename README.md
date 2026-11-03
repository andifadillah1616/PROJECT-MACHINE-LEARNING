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

# REFERENSI
Aguilar-Ruiz, J. S., & Michalak, M. (2024). Classification performance assessment for imbalanced multiclass data. Scientific Reports, 14, Article 10759. https://doi.org/10.1038/s41598-024-61365-z

Emami, S., & Martínez-Muñoz, G. (2025). Condensed-gradient boosting. International Journal of Machine Learning and Cybernetics, 16, 687–701. https://doi.org/10.1007/s13042-024-02279-0

Gunasekara, N., Pfahringer, B., Gomes, H., et al. (2024). Gradient boosted trees for evolving data streams. Machine Learning, 113, 3325–3352. https://doi.org/10.1007/s10994-024-06517-y

Pasaribu, J., Yudistira, N., & Mahmudy, W. F. (2024). Tabular data classification and regression: XGBoost or deep learning with retrieval-augmented generation. IEEE Access, 12, 191719–191732. https://doi.org/10.1109/ACCESS.2024.3518205

Wainer, J. (2024). An empirical evaluation of imbalanced data strategies from a practitioner’s point of view. Expert Systems with Applications, 256, Article 124863. https://doi.org/10.1016/j.eswa.2024.124863