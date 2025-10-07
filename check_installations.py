try:
    import pandas as pd
    print("✅ pandas installed")
except ImportError:
    print("❌ pandas not installed")

try:
    import sklearn
    print("✅ scikit-learn installed")
except ImportError:
    print("❌ scikit-learn not installed")

try:
    import streamlit
    print("✅ streamlit installed")
except ImportError:
    print("❌ streamlit not installed")

try:
    import joblib
    print("✅ joblib installed")
except ImportError:
    print("❌ joblib not installed")