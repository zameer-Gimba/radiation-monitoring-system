## Domain & Regulatory Guidance

As this project aims to align with real-world nuclear safety standards, we specifically seek expert input in the following areas:

### 1. Regulatory Compliance (NNRA/IAEA Standards)
*   **Threshold Validation:** Review the `radiation_levels.py` logic to ensure the simulated dosage triggers (Normal, Elevated, High) align with the Nigerian Nuclear Regulatory Authority or IAEA safety guidelines (Unclassified).
*   **Compliance Logging:** Feedback on the data logging format—what specific metadata (timestamping, sensor ID, calibration data) is required for a log to be considered "audit-ready" in a regulatory environment?

### 2. ICT Infrastructure & Data Integrity
*   **Secure Transmission:** Guidance on the most robust protocols (e.g., MQTT with TLS, Secure APIs) for transmitting sensor data from high-risk zones to central ICT servers.
*   **System Scalability:** Recommendations on database architecture for long-term storage of national radiation telemetry data.

### 3. Reporting & SOPs
*   **Incident Reporting:** Advice on the "Alert" output format. What information does a Deputy Manager or Director need to see immediately when an anomaly is detected?
*   **Standard Operating Procedures:** Suggestions for the README on how an operator should technically respond when the AI model flags a high-risk event.


#### Disclaimer
This project uses synthetic data for research purposes and does not contain real-time telemetry from any specific facility.
