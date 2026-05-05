import numpy as np
from sklearn.ensemble import IsolationForest

# Z-SCORE DETECTION
def z_score(series):
    mean = np.mean(series)
    std = np.std(series)
    return (series - mean) / std

def detect_anomalies_zscore(data, threshold=2.5):
    z_scores = z_score(data["radiation"])
    anomalies = np.where(np.abs(z_scores) > threshold)[0]
    return anomalies

# AI DETECTION (Isolation Forest)
def detect_anomalies_ai(data):
    model = IsolationForest(contamination=0.05, random_state=42)

    X = data[["radiation"]].values
    model.fit(X)

    preds = model.predict(X)

    anomalies = np.where(preds == -1)[0]
    return anomalies

# ENGINEERING THRESHOLD DETECTION
def detect_anomalies_threshold(data, upper=0.5, lower=0.0):
    anomalies = []

    for i, value in enumerate(data["radiation"]):
        if value > upper or value < lower:
            anomalies.append(i)

    return np.array(anomalies)
