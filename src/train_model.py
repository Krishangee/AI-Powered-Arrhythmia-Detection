import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
from sklearn.metrics import ConfusionMatrixDisplay
from sklearn.metrics import classification_report
import joblib
df=pd.read_csv("data/mitbih_train.csv",header=None)
x=df.iloc[:,0:187]
y=df.iloc[:,187]
x_train,x_test,y_train,y_test=train_test_split(
    x,
    y,
    test_size=0.2,
    random_state=42
)
print("Training Features:", x_train.shape)
print("Testing Features :", x_test.shape)
print("Training Labels  :", y_train.shape)
print("Testing Labels   :", y_test.shape)

model = RandomForestClassifier(
    random_state=42,
    class_weight="balanced"
)
model.fit(x_train,y_train)
joblib.dump(model, "arrhythmia_model.pkl")
print("Model saved successfully!")
print("Model trained successfully!")
# Make predictions
predictions = model.predict(x_test)

print("\nFirst 10 Predictions:")
print(predictions[:10])

print("\nActual Labels:")
print(y_test.values[:10])


accuracy = accuracy_score(y_test, predictions)

print("\nModel Accuracy:", accuracy)

cm=confusion_matrix(y_test,predictions)
print("\nConfusion Matrix:\n")
print(cm)
disp = ConfusionMatrixDisplay(
    confusion_matrix=cm,
    display_labels=["NORMAL","SVEB","VEB","FUSION","UNKNOWN"]
)


disp.plot(cmap="Blues")
plt.title("Confusion Matrix")
plt.show()

print("\nClassification Report:\n")
print(classification_report(
    y_test,
    predictions,target_names=[
        "NORMAL",
        "SVEB",
        "VEB",
        "FUSION",
        "UNKNOWN"
    ]
))