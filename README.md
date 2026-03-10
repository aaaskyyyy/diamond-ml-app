# Diamond Price Prediction Web App

## Deskripsi Project

Project ini merupakan implementasi **Machine Learning Regression** untuk memprediksi harga diamond berdasarkan karakteristiknya.

Model dilatih menggunakan dataset **diamonds.csv** dengan target variabel **price**.

Aplikasi web dibuat menggunakan **Streamlit** sehingga pengguna dapat memasukkan karakteristik diamond dan mendapatkan prediksi harga secara langsung.

---

## Fitur yang Digunakan

Model menggunakan fitur berikut:

* carat
* cut
* color
* clarity
* depth
* table
* x
* y
* z

---

## Algoritma Machine Learning

Model dilatih menggunakan algoritma:

* XGBoost Regressor

Encoding fitur kategori dilakukan menggunakan:

* LabelEncoder

---

## Struktur Folder Project

```
diamond-ml-app
│
├── venv/
├── app.py
├── diamonds.csv
├── diamond_price_model.pkl
├── le_cut.pkl
├── le_color.pkl
├── le_clarity.pkl
├── requirements.txt
└── README.md
```

---

## Cara Menjalankan Project

### 1. Clone atau Download Project

Pastikan semua file berada dalam satu folder project.

---

### 2. Aktifkan Virtual Environment

Windows:

```
env\Scripts\activate
```

---

### 3. Install Dependencies

```
pip install -r requirements.txt
```

---

### 4. Jalankan Aplikasi Streamlit

```
streamlit run app.py
```

---

### 5. Buka di Browser

Aplikasi akan berjalan di:

```
http://localhost:8501
```

---

## Cara Menggunakan Aplikasi

1. Masukkan nilai fitur diamond:

   * carat
   * cut
   * color
   * clarity
   * depth
   * table
   * x
   * y
   * z

2. Klik tombol **Predict Price**

3. Aplikasi akan menampilkan **prediksi harga diamond**.

---

## Library yang Digunakan

* streamlit
* pandas
* numpy
* scikit-learn
* xgboost
* joblib

---

## Author

Project ini dibuat sebagai tugas mata kuliah **Machine Learning**.
