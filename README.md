# ☢️ Radiation Leakage Monitoring & Containment Integrity System

## Overview
This project simulates a nuclear facility monitoring system designed to detect radiation leakage and containment anomalies using engineering thresholds, statistical analysis, and machine learning.

## Problem
Failure to detect abnormal radiation levels early can lead to:
- Environmental contamination
- Health hazards
- System shutdowns
- Regulatory violations

## Features
- Simulated radiation data (normal, spike, degradation)
- Threshold-based safety monitoring
- Z-score anomaly detection
- AI-based anomaly detection (Isolation Forest)
- Visualization with safe operating zone

## How It Works
1. Radiation levels are simulated
2. System checks:
   - Safety thresholds
   - Statistical deviation
   - AI anomalies
3. Anomalies are highlighted visually

## Run

```bash
pip install -r requirements.txt
python main.py
```
### Authors
Muhammad Ibrahim Gimba
Yahya Shuaibu
