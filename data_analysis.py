import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print("=== Smart Agriculture Data Analysis ===")

# Dataset load karo
try:
    df = pd.read_csv('Crop_recommendation.csv')
    print("✅ Dataset successfully loaded!")
except:
    print("❌ Dataset load nahi hua. File ka naam check karo.")
    exit()

# Basic info
print(f"\n📊 Dataset Shape: {df.shape}")
print(f"🌾 Unique Crops: {df['label'].nunique()}")
print(f"📝 Crops List: {df['label'].unique()}")

# First 5 rows dekho
print("\n📋 Pehle 5 rows:")
print(df.head())

# Missing values check
print("\n🔍 Missing Values Check:")
print(df.isnull().sum())

# Basic statistics
print("\n📈 Basic Statistics:")
print(df.describe())

# Crops distribution
print("\n🌱 Crops Distribution:")
print(df['label'].value_counts())

# Visualization - optional (agar matplotlib work kare toh)
try:
    plt.figure(figsize=(10, 6))
    df['label'].value_counts().plot(kind='bar')
    plt.title('Crops Distribution')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
except:
    print("📊 Visualization skip kar rahe hain...")