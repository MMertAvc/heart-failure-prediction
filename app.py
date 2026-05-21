import streamlit as st
import joblib
import numpy as np

# Modeli yükle
model = joblib.load('model.pkl')

st.title("Heart Failure Risk Prediction")

# Giriş özellikleri
age = st.slider("Age", 20, 100, 55)
sex = st.selectbox("Sex (0 = Female, 1 = Male)", [0, 1])
cp = st.selectbox("Chest Pain Type (0–3)", [0, 1, 2, 3])
trestbps = st.number_input("Resting Blood Pressure", value=120)
chol = st.number_input("Cholesterol", value=200)
fbs = st.selectbox("Fasting Blood Sugar > 120 (1 = Yes)", [0, 1])
restecg = st.selectbox("Resting ECG (0–2)", [0, 1, 2])
thalach = st.number_input("Maximum Heart Rate Achieved", value=150)
exang = st.selectbox("Exercise Induced Angina (1 = Yes)", [0, 1])
oldpeak = st.number_input("Oldpeak (ST depression)", value=1.0)
slope = st.selectbox("Slope of ST segment", [0, 1, 2])

# Özellik vektörü
features = np.array([[age, sex, cp, trestbps, chol, fbs, restecg,
                      thalach, exang, oldpeak, slope]])

# Tahmin
if st.button("Predict"):
    pred = model.predict(features)[0]
    st.success("Prediction: " + ("Heart Disease Risk ✅" if pred == 1 else "No Risk ❌"))
