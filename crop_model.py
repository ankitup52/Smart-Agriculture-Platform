import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib
import os

print("=== Training Crop Recommendation Model ===")

# Check if dataset exists
if not os.path.exists('Crop_recommendation.csv'):
    print("❌ Dataset file nahi mili!")
    print("💡 Check karo:")
    print("1. File ka naam 'Crop_recommendation.csv' hai?")
    print("2. Same folder mein hai?")
    exit()

# Data load karo
try:
    df = pd.read_csv('Crop_recommendation.csv')
    print("✅ Dataset loaded successfully!")
except Exception as e:
    print(f"❌ Dataset load nahi hui: {e}")
    exit()

print(f"📊 Dataset Shape: {df.shape}")
print(f"🌾 Columns: {df.columns.tolist()}")

# Features aur target alag karo
X = df[['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall']]
y = df['label']

print(f"🎯 Target classes: {len(y.unique())}")

# Data ko train aur test mein divide karo
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Model train karo
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Predictions karo
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"✅ Model Accuracy: {accuracy:.4f} ({accuracy*100:.2f}%)")

# Model save karo
joblib.dump(model, 'crop_recommendation_model.pkl')
print("💾 Model saved successfully!")

# Test prediction
test_sample = X_test.iloc[0:1]
predicted_crop = model.predict(test_sample)[0]
print(f"🧪 Test Prediction: {predicted_crop}")