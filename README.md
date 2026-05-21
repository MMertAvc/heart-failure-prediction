# Heart Failure Prediction — Binary Classification

A machine learning project that predicts heart disease risk from patient clinical data using a Random Forest classifier, with a Streamlit web application for real-time risk assessment.

---

## English

### About

This project trains a binary classifier to predict whether a patient is at risk of heart failure based on clinical measurements such as age, blood pressure, cholesterol, and ECG results. The trained model is saved and served through a Streamlit web app where users can enter patient data and receive an instant risk prediction.

### Features

- Binary classification: heart disease risk (1) vs. no risk (0)
- Input features: age, sex, chest pain type, resting BP, cholesterol, fasting blood sugar, ECG, max heart rate, exercise-induced angina, ST depression, slope, vessels, thalassemia
- Random Forest classifier (`model.pkl`)
- Streamlit web app for patient-level risk assessment

### Dataset

**Source:** [Kaggle — Heart Failure Prediction](https://www.kaggle.com/datasets/fedesoriano/heart-failure-prediction)

| File | Size | Status |
|---|---|---|
| `heart.csv` | 30 KB | ✅ Included |

918 patient records with 11 clinical features and a binary `HeartDisease` target.

### Model Architecture / Tech Stack

```
Patient Clinical Data (11 features)
→ Feature Engineering + Preprocessing
→ Random Forest Classifier
→ Binary Output: Heart Disease (1) / No Disease (0)
```

**Tech Stack:** Python · scikit-learn · pandas · NumPy · joblib · Streamlit

### How to Run

```bash
pip install -r requirements.txt
streamlit run app.py
```

Enter patient clinical values in the Streamlit app to get an instant heart disease risk prediction.

### Requirements

```
pandas
numpy
scikit-learn
streamlit
joblib
```

---

## Türkçe

### Hakkında

Bu proje, yaş, kan basıncı, kolesterol ve EKG sonuçları gibi klinik ölçümler temelinde bir hastanın kalp yetmezliği riskini tahmin etmek için ikili bir sınıflandırıcı eğitir. Eğitilen model kaydedilerek bir Streamlit web uygulamasıyla sunulur; kullanıcılar hasta verilerini girerek anında risk tahmini alabilir.

### Özellikler

- İkili sınıflandırma: kalp hastalığı riski (1) / risk yok (0)
- Giriş özellikleri: yaş, cinsiyet, göğüs ağrısı türü, istirahat kan basıncı, kolesterol, açlık kan şekeri, EKG, maksimum kalp atışı, egzersizle anjina, ST depresyonu, eğim, damarlar, talasemi
- Rastgele Orman sınıflandırıcısı (`model.pkl`)
- Hasta düzeyinde risk değerlendirmesi için Streamlit web uygulaması

### Veri Seti

**Kaynak:** [Kaggle — Kalp Yetmezliği Tahmini](https://www.kaggle.com/datasets/fedesoriano/heart-failure-prediction)

| Dosya | Boyut | Durum |
|---|---|---|
| `heart.csv` | 30 KB | ✅ Dahil |

11 klinik özellik ve ikili `HeartDisease` hedefiyle 918 hasta kaydı.

### Model Mimarisi / Teknoloji Yığını

```
Hasta Klinik Verisi (11 özellik)
→ Özellik Mühendisliği + Ön İşleme
→ Rastgele Orman Sınıflandırıcısı
→ İkili Çıkış: Kalp Hastalığı (1) / Hastalık Yok (0)
```

**Teknoloji Yığını:** Python · scikit-learn · pandas · NumPy · joblib · Streamlit

### Nasıl Çalıştırılır

```bash
pip install -r requirements.txt
streamlit run app.py
```

Streamlit uygulamasına hasta klinik değerlerini girerek anında kalp hastalığı risk tahmini alın.

### Gereksinimler

```
pandas
numpy
scikit-learn
streamlit
joblib
```
