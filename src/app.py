import streamlit as st
import joblib
import pandas as pd
import matplotlib.pyplot as plt
st.title("❤️ AI-Powered Arrhythmia Detection")

st.write("Welcome to the Arrhythmia Detection System!")

st.write("This application uses a trained Random Forest model to classify ECG heartbeats.")

model = joblib.load("../arrhythmia_model.pkl")

df = pd.read_csv("../demo_data.csv", header=None)

sample_number = st.selectbox(
    "Select ECG Sample",
    df.index
)

sample = df.iloc[sample_number, :187]
sample = sample.values.reshape(1, -1)
actual_label = int(df.iloc[sample_number, 187])
st.subheader("ECG Heartbeat Classification")

if st.button("Predict Heartbeat"):
    

    prediction = model.predict(sample)
    probabilities = model.predict_proba(sample)
    class_names = {
    0: "❤️ NORMAL",
    1: "⚠️ SVEB (Supraventricular Ectopic Beat)",
    2: "⚠️ VEB (Ventricular Ectopic Beat)",
    3: "⚠️ FUSION Beat",
    4: "❓ UNKNOWN Beat"
}
    

    st.success(f"Predicted Heartbeat: {class_names[int(prediction[0])]}")
    confidence = probabilities.max() * 100
    st.write(f"### Confidence: {confidence:.2f}%")
    descriptions = {
    0: "Normal heartbeat with no detected abnormality.",
    1: "Supraventricular ectopic beat originating above the ventricles.",
    2: "Ventricular ectopic beat originating from the ventricles.",
    3: "Fusion beat formed by both normal and ventricular impulses.",
    4: "Heartbeat could not be classified into the known categories."
}
    st.write("### Actual Label:")
    st.info(class_names[actual_label])
    if int(prediction[0]) == actual_label:
        st.success("✅ Correct Prediction")
    else:
        st.error("❌ Incorrect Prediction")
    st.info(descriptions[int(prediction[0])])
    fig, ax = plt.subplots(figsize=(10,4))
    ax.plot(sample.flatten())
    ax.set_title("ECG Waveform")
    ax.set_xlabel("Samples")
    ax.set_ylabel("Amplitude")
    ax.grid(True)
    st.pyplot(fig)

st.sidebar.title("Project Information")

st.sidebar.write("Model: Random Forest")
st.sidebar.write("Dataset: MIT-BIH Arrhythmia")
st.sidebar.write("Accuracy: 97.84%")
st.sidebar.write("Classes: 5")
st.markdown("---")
st.caption(
    "Developed by Krishangee Handique | B.Tech ECE | VIT Bhopal"
)
st.markdown("---")
st.warning(
    "This application is for educational purposes only and is not intended for clinical diagnosis."
)