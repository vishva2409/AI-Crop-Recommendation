# src/soil_analysis.py
import pandas as pd

def analyze_soil(soil_sample):
    """
    soil_sample: dict with keys N, P, K, pH, Moisture
    Returns: dict with analysis and suggested actions
    """
    analysis = {}
    
    # Simple thresholds (example, adjust as needed)
    if soil_sample['N'] < 80:
        analysis['Nitrogen'] = "Low - add nitrogen fertilizer"
    else:
        analysis['Nitrogen'] = "Good"

    if soil_sample['P'] < 30:
        analysis['Phosphorus'] = "Low - add phosphorus fertilizer"
    else:
        analysis['Phosphorus'] = "Good"

    if soil_sample['K'] < 30:
        analysis['Potassium'] = "Low - add potassium fertilizer"
    else:
        analysis['Potassium'] = "Good"

    if soil_sample['pH'] < 6.0:
        analysis['pH'] = "Acidic - consider liming"
    elif soil_sample['pH'] > 7.5:
        analysis['pH'] = "Alkaline - consider sulfur"
    else:
        analysis['pH'] = "Optimal"

    if soil_sample['Moisture'] < 20:
        analysis['Moisture'] = "Dry - irrigation needed"
    else:
        analysis['Moisture'] = "Good"

    return analysis

# Example usage
if __name__ == "__main__":
    sample = {'N': 70, 'P': 25, 'K': 40, 'pH': 5.8, 'Moisture': 15}
    result = analyze_soil(sample)
    for k,v in result.items():
        print(k, ":", v)
