<div align="center">

# ❤️ AI-Powered Arrhythmia Detection

### Machine Learning Project for ECG Heartbeat Classification using Random Forest and Streamlit

![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Random%20Forest-orange?logo=scikitlearn)
![Streamlit](https://img.shields.io/badge/Streamlit-Web%20App-red?logo=streamlit)
![License](https://img.shields.io/badge/License-MIT-green)

**Developed by:** **Krishangee Handique**

🔗 **GitHub:** https://github.com/Krishangee

</div>

---

An end-to-end Machine Learning project that classifies ECG heartbeats into five categories using the MIT-BIH Arrhythmia Dataset. The project performs ECG heartbeat classification using a Random Forest classifier and provides an interactive Streamlit web application for heartbeat prediction, confidence estimation, label comparison, and ECG waveform visualization.

---

# 📖 Overview

Electrocardiogram (ECG) signals are widely used for detecting abnormalities in heart rhythm. In this project, a Random Forest classifier is trained on the MIT-BIH Arrhythmia Dataset to classify ECG heartbeats into five heartbeat categories.

The application allows users to:

- Select an ECG sample
- Predict the heartbeat category
- View model confidence
- Compare predicted and actual labels
- Visualize ECG waveform
- Understand heartbeat abnormalities

---

# ✨ Project Highlights

- Trained a Random Forest classifier on the MIT-BIH Arrhythmia Dataset.
- Achieved **97.84% test accuracy**.
- Supports classification of **5 heartbeat classes**.
- Interactive Streamlit web application.
- Displays prediction confidence.
- Compares predicted label with the actual label.
- Visualizes ECG heartbeat waveform.
- Built using Scikit-learn, Pandas, NumPy and Streamlit.

---

# 🚀 Features

- End-to-end ECG heartbeat classification
- ECG preprocessing and feature preparation
- Random Forest machine learning model
- Prediction confidence score
- Actual vs Predicted heartbeat comparison
- ECG waveform visualization
- Interactive Streamlit dashboard
- Model evaluation using:
  - Accuracy
  - Precision
  - Recall
  - F1-score
  - Confusion Matrix
  - Classification Report

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
- **1 Class Label**

Heartbeat Categories

| Label | Heartbeat Type |
|------:|----------------|
| 0 | Normal Beat |
| 1 | Supraventricular Ectopic Beat (SVEB) |
| 2 | Ventricular Ectopic Beat (VEB) |
| 3 | Fusion Beat |
| 4 | Unknown Beat |

## Dataset Download

The dataset is **not included** in this repository because it exceeds GitHub's file size limit.

Download it from:

https://www.kaggle.com/datasets/shayanfazeli/heartbeat

After downloading, place the CSV files inside the **data/** folder.

---

# 📈 Model Performance

The Random Forest classifier achieved excellent performance on the MIT-BIH Arrhythmia Dataset.

| Metric | Value |
|---------|-------|
| Accuracy | **97.84%** |
| Number of Classes | 5 |
| Model | Random Forest |

The model was evaluated using:

- Accuracy
- Precision
- Recall
- F1-score
- Confusion Matrix
- Classification Report

Although the overall accuracy is high, recall remains important because it measures how well the model detects minority heartbeat classes such as SVEB and Fusion beats.

---

# 📁 Project Structure

```text
AI-Powered-Arrhythmia-Detection/
│
├── data/
│   └── Place downloaded dataset here
│
├── screenshots/
│
├── docs/
│
├── src/
│   ├── app.py
│   ├── train_model.py
│   ├── predict.py
│   ├── preprocessing.py
│   ├── filter_signal.py
│   ├── r_peak_detection.py
│   ├── model_preparation.py
│   ├── data_analysis.py
│   ├── visualization.py
│   └── load_ecg.py
│
├── arrhythmia_model.pkl
├── requirements.txt
├── README.md
├── LICENSE
└── .gitignore
```

---

# 📸 Screenshots

## Home Page

![Home Page](screenshots/home_page.png)

---

## Normal Heartbeat Prediction

![Normal Prediction](screenshots/predicted_normal.png)

---

## Fusion Beat Prediction

![Fusion Prediction](screenshots/predicted_fusion.png)

---

## Unknown Heartbeat Prediction

![Unknown Prediction](screenshots/predicted_unknown.png)

---

## Confusion Matrix

![Confusion Matrix](screenshots/confusion_matrix.png)

---

## Classification Report

![Classification Report](screenshots/classification_report.png)

---

# ⚙️ Installation

## 1. Clone the Repository

```bash
git clone https://github.com/Krishangee/AI-Powered-Arrhythmia-Detection.git
```

## 2. Navigate to the Project Folder

```bash
cd AI-Powered-Arrhythmia-Detection
```

## 3. Install Required Libraries

```bash
pip install -r requirements.txt
```

## 4. Download Dataset

Download the MIT-BIH Arrhythmia Dataset from Kaggle and place the CSV files inside the **data/** folder.

## 5. Run the Streamlit Application

```bash
cd src
streamlit run app.py
```

---

# 💻 Technologies Used

| Category | Technology |
|-----------|------------|
| Programming Language | Python |
| Machine Learning | Scikit-learn |
| Algorithm | Random Forest |
| Data Processing | Pandas, NumPy |
| Visualization | Matplotlib |
| Web Framework | Streamlit |
| Model Serialization | Joblib |
| Dataset | MIT-BIH Arrhythmia Dataset |

---

# 📊 Results

The Random Forest classifier achieved an overall accuracy of **97.84%** while classifying ECG heartbeats into five heartbeat categories.

### Evaluation Metrics

- Accuracy: **97.84%**
- Precision: High across most heartbeat classes
- Recall: Strong overall performance with comparatively lower recall for minority heartbeat classes
- F1-score: Balanced performance across all heartbeat categories

The application also displays:

- Prediction confidence
- Actual heartbeat label
- Prediction correctness
- ECG waveform visualization

---

# ⚠️ Limitations

- Dataset is highly imbalanced.
- Minority heartbeat classes are harder to classify accurately.
- The application is intended for educational and research purposes only.
- Not suitable for clinical diagnosis.

---

# 🚀 Future Improvements

- Train Deep Learning models such as CNN and LSTM.
- Support user-uploaded ECG signals.
- Improve minority heartbeat classification.
- Deploy on Streamlit Community Cloud.
- Evaluate on additional ECG datasets.
- Add explainable AI (XAI) visualization.

---

# 👨‍💻 Author

**Krishangee Handique**

B.Tech Electronics and Communication Engineering

VIT Bhopal University

📧 Email: krisdig30@gmail.com

🔗 GitHub: https://github.com/Krishangee

---

# 📄 License

This project is licensed under the **MIT License**.

---



© 2026 Krishangee Handique