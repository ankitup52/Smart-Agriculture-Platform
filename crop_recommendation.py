import pandas as pd
import numpy as np
import streamlit as st

class CropRecommender:
    def __init__(self):
        self.df = None
        self.load_data()
    
    def load_data(self):
        """Load crop recommendation dataset"""
        try:
            self.df = pd.read_csv('Crop_recommendation.csv')
            st.success(f"✅ Crop dataset loaded: {len(self.df)} records")
        except Exception as e:
            st.error(f"❌ Error loading crop dataset: {e}")
            self.df = None
    
    def recommend_crop(self, N, P, K, temperature, humidity, ph, rainfall):
        """Recommend crop based on parameters"""
        if self.df is None:
            # Fallback logic if dataset not available
            return self.fallback_recommendation(N, P, K, temperature, humidity, ph, rainfall)
        
        try:
            # Simple rule-based recommendation
            conditions = []
            
            # Rice prefers high rainfall and humidity
            if rainfall > 150 and humidity > 70:
                conditions.append('rice')
            
            # Wheat prefers moderate conditions
            if 20 <= temperature <= 25 and 50 <= humidity <= 80:
                conditions.append('wheat')
            
            # Maize needs good nitrogen
            if N > 70 and temperature > 25:
                conditions.append('maize')
            
            # Chickpea needs less water
            if rainfall < 100 and ph > 6.5:
                conditions.append('chickpea')
            
            if conditions:
                return np.random.choice(conditions), 0.85
            else:
                return self.fallback_recommendation(N, P, K, temperature, humidity, ph, rainfall)
                
        except:
            return self.fallback_recommendation(N, P, K, temperature, humidity, ph, rainfall)
    
    def fallback_recommendation(self, N, P, K, temperature, humidity, ph, rainfall):
        """Fallback recommendation logic"""
        crops = ['rice', 'wheat', 'maize', 'chickpea', 'sugarcane', 'cotton']
        
        # Simple scoring system
        scores = {}
        for crop in crops:
            score = 0
            
            if crop == 'rice':
                if rainfall > 150: score += 3
                if humidity > 70: score += 2
                if temperature > 25: score += 1
                
            elif crop == 'wheat':
                if 20 <= temperature <= 25: score += 3
                if 6 <= ph <= 7.5: score += 2
                if 50 <= humidity <= 80: score += 1
                
            elif crop == 'maize':
                if N > 60: score += 3
                if temperature > 25: score += 2
                if rainfall > 100: score += 1
                
            elif crop == 'chickpea':
                if rainfall < 100: score += 3
                if ph > 6.5: score += 2
                if 20 <= temperature <= 30: score += 1
                
            scores[crop] = score
        
        recommended = max(scores, key=scores.get)
        confidence = min(0.70 + (scores[recommended] * 0.05), 0.95)
        
        return recommended, confidence

def get_crop_info(crop_name):
    """Get information about recommended crop"""
    crop_db = {
        'rice': {
            'sowing_time': 'June-July (Kharif)',
            'harvest_time': 'October-November',
            'water_needs': 'High (flooded fields)',
            'soil_type': 'Clayey loam',
            'season': 'Kharif',
            'fertilizer': 'NPK 40-20-20 kg/ha'
        },
        'wheat': {
            'sowing_time': 'November-December (Rabi)',
            'harvest_time': 'March-April',
            'water_needs': 'Moderate',
            'soil_type': 'Well-drained loam',
            'season': 'Rabi',
            'fertilizer': 'NPK 20-20-0 at sowing'
        },
        'maize': {
            'sowing_time': 'June-July (Kharif)',
            'harvest_time': 'September-October',
            'water_needs': 'Moderate',
            'soil_type': 'Well-drained soil',
            'season': 'Kharif',
            'fertilizer': 'NPK 60-40-20 kg/acre'
        },
        'chickpea': {
            'sowing_time': 'October-November (Rabi)',
            'harvest_time': 'February-March',
            'water_needs': 'Low',
            'soil_type': 'Sandy loam',
            'season': 'Rabi',
            'fertilizer': '20-40 kg N/ha, 40-60 kg P2O5/ha'
        }
    }
    return crop_db.get(crop_name.lower(), {
        'sowing_time': 'Consult local agriculture officer',
        'harvest_time': 'Varies by region',
        'water_needs': 'Moderate',
        'soil_type': 'Well-drained soil',
        'season': 'Depends on region',
        'fertilizer': 'Based on soil test results'
    })