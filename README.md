# ☢️ Radiation Leakage Monitoring & Containment Integrity System

## Project Overview
This project simulates a nuclear facility monitoring system designed to detect radiation leakage and containment anomalies using engineering thresholds, statistical analysis, and machine learning.

**Objective:** To provide a robust, AI-driven monitoring framework applicable to nuclear research centers, medical radiotherapy units, and industrial facilities globally, ensuring compliance with international safety standards (IAEA).

**Aim:** To develop and simulate an automated Radiological Surveillance System that utilizes AI to detect anomalies in radiation telemetry, providing real-time alerts and generating standardized compliance reports for facility safety officers.

## Problem
Manual radiation monitoring in some facicilies around the world faces challenges with real-time data logging and anomaly detection. This project aims to automate that process.

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
## Disclaimer
This project uses synthetic data for research purposes and does not contain real-time telemetry from any specific facility or any unclassified information.

### Authors
Muhammad Ibrahim Gimba

Yahya Shuaibu
