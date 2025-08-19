# 🛡️ IoT Anomaly Detector

Detect unusual IoT device activity using data science and lightweight ML.

> **Goal:** Give small teams a simple way to spot suspicious behavior in IoT logs (requests, ports, bytes, timing) and surface clear, human-readable insights.

---

## 🔎 Problem
IoT devices are noisy and always on. Abnormal traffic (port scans, beaconing, data exfiltration) hides inside normal flows. Many teams lack a simple detector and an explainable report.

**This project provides:**
- Quick EDA to understand device behavior
- Baseline anomaly models (Isolation Forest / One-Class SVM)
- Simple scoring + alert rules
- A clean report/dashboard (Streamlit) for non-experts

---

## 🧰 Tech Stack
- **Python**, **Pandas**, **NumPy**
- **scikit-learn** (Isolation Forest, One-Class SVM)
- **Matplotlib**
- **Streamlit** (light dashboard)

---

## 📁 Repository Structure
