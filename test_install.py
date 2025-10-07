try:
    import pandas as pd
    print("✅ Pandas installed")
    
    import sklearn
    print("✅ Scikit-learn installed")
    
    import joblib
    print("✅ Joblib installed")
    
    print("\n🎉 All packages installed successfully!")
    
except ImportError as e:
    print(f"❌ Error: {e}")