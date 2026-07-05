# ❤️ AI-Powered Arrhythmia Detection

<p align="center">

[![Python](https://img.shields.io/badge/Python-3.12-blue?style=for-the-badge&logo=python)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-Live_App-red?style=for-the-badge&logo=streamlit)](https://ai-powered-arrhythmia-detection-ykutrdayhxwvgqsknjdwh4.streamlit.app/)
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Random_Forest-orange?style=for-the-badge&logo=scikitlearn)]
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)]

</p>

An end-to-end Machine Learning project that classifies ECG heartbeats into **five heartbeat categories** using the **MIT-BIH Arrhythmia Dataset**. The project includes ECG preprocessing, Random Forest classification, model evaluation, and an interactive Streamlit web application for heartbeat prediction and visualization.

---

# 🚀 Live Demo

### 🌐 Try the application here

**https://ai-powered-arrhythmia-detection-ykutrdayhxwvgqsknjdwh4.streamlit.app/**

---

# 📌 Overview

Electrocardiogram (ECG) signals are widely used to detect abnormalities in heart rhythm.

This project builds an end-to-end ECG heartbeat classification system using the **MIT-BIH Arrhythmia Dataset** and a **Random Forest Classifier**.

The application allows users to:

- Select an ECG heartbeat sample
- Predict the heartbeat category
- View prediction confidence
- Compare predicted and actual labels
- Visualize the ECG waveform

---

# ✨ Project Highlights

- Trained a Random Forest classifier on the MIT-BIH Arrhythmia Dataset
- Achieved **97.84% test accuracy**
- Supports classification of **5 heartbeat classes**
- Interactive Streamlit web application
- ECG waveform visualization
- Prediction confidence score
- Confusion Matrix and Classification Report

---

# 🛠 Features

- End-to-end ECG heartbeat classification
- ECG preprocessing
- Feature preparation
- Random Forest classifier
- Model evaluation
- Streamlit web application
- ECG waveform visualization
- Prediction confidence
- Actual vs Predicted label comparison

---

# 🔄 Project Workflow

```text
MIT-BIH Arrhythmia Dataset
            │
            ▼
     Data Preprocessing
            │
            ▼
    Feature Preparation
            │
            ▼
     Train-Test Split
            │
            ▼
 Random Forest Classifier
            │
            ▼
   Model Evaluation
            │
            ▼
 Streamlit Web Application
            │
            ▼
 ECG Heartbeat Prediction
```

---

# 📂 Dataset

This project uses the **MIT-BIH Arrhythmia Dataset**, one of the most widely used benchmark datasets for ECG heartbeat classification.

Each heartbeat contains:

- **187 ECG signal values**
- **1 class label**

| Label | Heartbeat Type |
|------:|----------------|
| 0 | Normal Beat |
| 1 | Supraventricular Ectopic Beat (SVEB) |
| 2 | Ventricular Ectopic Beat (VEB) |
| 3 | Fusion Beat |
| 4 | Unknown Beat |

## Dataset Download

The original dataset is **not included** in this repository because it exceeds GitHub's file size limit.

Download it from:

https://www.kaggle.com/datasets/shayanfazeli/heartbeat

After downloading, place the dataset inside the **data/** folder.

---

# 📊 Model Performance

| Metric | Value |
|---------|-------|
| Accuracy | **97.84%** |
| Model | Random Forest |
| Classes | 5 |

Evaluation Metrics:

- Accuracy
- Precision
- Recall
- F1-score
- Confusion Matrix
- Classification Report

---

# 📁 Project Structure

```text
AI-Powered-Arrhythmia-Detection/
│
├── data/
│
├── docs/
│
├── plots/
│
├── screenshots/
│
├── src/
│   ├── app.py
│   ├── train_model.py
│   ├── predict.py
│   ├── preprocessing.py
│   ├── filter_signal.py
│   ├── r_peak_detection.py
│   ├── visualization.py
│   ├── load_ecg.py
│   ├── data_analysis.py
│   └── model_preparation.py
│
├── demo_data.csv
├── arrhythmia_model.pkl
├── requirements.txt
├── README.md
├── LICENSE
└── .gitignore
```

---

# 📷 Screenshots

## Home Page

![Home Page](screenshots/home_page.png)

---

## Normal Beat Prediction

![Normal Prediction](screenshots/predicted_normal.png)

---

## Fusion Beat Prediction

![Fusion Prediction](screenshots/predicted_fusion.png)

---

## Unknown Beat Prediction

![Unknown Prediction](screenshots/predicted_unknown.png)

---

## Confusion Matrix

![Confusion Matrix](screenshots/confusion_matrix.png)

---

## Classification Report

![Classification Report](screenshots/classification_report.png)

---

# ⚙ Installation

## Clone Repository

```bash
git clone https://github.com/Krishangee/AI-Powered-Arrhythmia-Detection.git
```

## Go to Project Directory

```bash
cd AI-Powered-Arrhythmia-Detection
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Run Streamlit App

```bash
cd src
streamlit run app.py
```

---

# 🧪 Technologies Used

### Programming Language

- Python

### Machine Learning

- Scikit-learn
- Random Forest Classifier

### Data Processing

- Pandas
- NumPy

### Visualization

- Matplotlib

### Web Framework

- Streamlit

### Model Serialization

- Joblib

---

# 📈 Results

The trained Random Forest classifier achieved:

| Metric | Value |
|---------|-------|
| Accuracy | **97.84%** |
| Classes | 5 |
| Model | Random Forest |

Performance evaluated using:

- Accuracy
- Precision
- Recall
- F1-score
- Confusion Matrix
- Classification Report

---

# ⚠ Limitations

- Dataset is highly imbalanced.
- Minority heartbeat classes are harder to classify.
- Intended for educational and research purposes only.
- Not suitable for clinical diagnosis.

---

# 🚀 Future Improvements

- Deep Learning models (1D CNN, LSTM)
- User ECG upload
- Better minority class performance
- Cloud deployment enhancements
- Support additional ECG datasets

---

# 👩‍💻 Author

**Krishangee Handique**

B.Tech Electronics & Communication Engineering

VIT Bhopal University

📧 Email: krisdig30@gmail.com

🔗 GitHub: https://github.com/Krishangee

🌐 Live Demo:

https://ai-powered-arrhythmia-detection-ykutrdayhxwvgqsknjdwh4.streamlit.app/

---

# 📜 License

This project is licensed under the **MIT License**.