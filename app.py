import streamlit as st
import pandas as pd
import numpy as np
import joblib

# ===============================
# LOAD MODEL DAN ENCODER
# ===============================

model = joblib.load("diamond_price_model.pkl")

le_cut = joblib.load("le_cut.pkl")
le_color = joblib.load("le_color.pkl")
le_clarity = joblib.load("le_clarity.pkl")

# ===============================
# JUDUL APLIKASI
# ===============================

st.title("Diamond Price Prediction")
st.write("Masukkan karakteristik diamond untuk memprediksi harga")

# ===============================
# INPUT USER
# ===============================

carat = st.number_input("Carat", min_value=0.0)

cut = st.selectbox(
    "Cut",
    ["Fair","Good","Very Good","Premium","Ideal"]
)

color = st.selectbox(
    "Color",
    ["D","E","F","G","H","I","J"]
)

clarity = st.selectbox(
    "Clarity",
    ["I1","SI2","SI1","VS2","VS1","VVS2","VVS1","IF"]
)

depth = st.number_input("Depth", min_value=0.0)
table = st.number_input("Table", min_value=0.0)

x = st.number_input("Length (x)", min_value=0.0)
y = st.number_input("Width (y)", min_value=0.0)
z = st.number_input("Depth (z)", min_value=0.0)

# ===============================
# ENCODING
# ===============================

cut_encoded = le_cut.transform([cut])[0]
color_encoded = le_color.transform([color])[0]
clarity_encoded = le_clarity.transform([clarity])[0]

# ===============================
# PREDIKSI
# ===============================

if st.button("Predict Price"):

    input_data = pd.DataFrame({
        "carat":[carat],
        "cut":[cut_encoded],
        "color":[color_encoded],
        "clarity":[clarity_encoded],
        "depth":[depth],
        "table":[table],
        "x":[x],
        "y":[y],
        "z":[z]
    })

    prediction = model.predict(input_data)

    st.success(f"Estimated Diamond Price: ${prediction[0]:,.2f}")