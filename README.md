# 🛡️ NEXUS-IDS

### Intelligent Network Intrusion Detection System

An end-to-end Machine Learning system for detecting malicious network traffic using the **UNSW-NB15** dataset.

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

---

## 📖 Overview

**NEXUS-IDS** is a Machine Learning-based Intrusion Detection System (IDS) that classifies network traffic as **normal** or **malicious**. It uses multiple ML algorithms trained on the **UNSW-NB15** dataset and is deployed through an interactive **Streamlit** web application.

---

## ✨ Features

- 🔍 Detects 9 types of network attacks + normal traffic
- 🤖 Multiple ML models (Logistic Regression, SVM, Random Forest)
- 🏆 Voting Ensemble model for higher accuracy
- 📊 Interactive Streamlit dashboard
- ⚡ Real-time prediction from user input

---

## 🧠 Machine Learning Models

| Model | Description |
|-------|-------------|
| Logistic Regression | Baseline linear classifier |
| SVM | Kernel-based classifier |
| Random Forest | Ensemble of decision trees |
| **Voting Ensemble** | **Best performing model** ⭐ |

---

## 📊 Dataset — UNSW-NB15

- **Source:** UNSW Canberra Cyber Range Lab
- **Records:** ~2.5 million
- **Features:** 49 features
- **Attack Categories:** Fuzzers, Analysis, Backdoors, DoS, Exploits, Generic, Reconnaissance, Shellcode, Worms

---

## 🚀 Getting Started

### 1. Clone the repository

git clone https://github.com/ahmedashraf23413/NEXUS-IDS-Intelligent-Network-Intrusion-Detection-System.git
cd NEXUS-IDS-Intelligent-Network-Intrusion-Detection-System

### 2. Install dependencies

pip install -r requirements.txt

### 3. Run the app

streamlit run app1.py

---

## 📁 Project Structure

NEXUS-IDS/
├── app1.py                        # Streamlit application
├── cyper.ipynb                    # Model training & analysis
├── columns.pkl                    # Saved feature columns
├── ensemble_model.pkl             # Trained ensemble model
├── onehot_encoder.pkl             # Categorical encoder
├── requirements.txt               # Python dependencies
├── data/                          # Dataset files
│   └── UNSW_NB15_training-set.parquet
└── analysis project/              # EDA & analysis files

---

## 📸 Screenshots

<img width="1907" height="1007" alt="Screenshot 2026-09-11 153138" src="https://github.com/user-attachments/assets/eb64cf59-bf6c-4a06-87aa-221471f3d4ea" />

---

## 🛠️ Tech Stack

- **Language:** Python 3.10+
- **ML Libraries:** scikit-learn, pandas, numpy
- **Web Framework:** Streamlit
- **Version Control:** Git + Git LFS

---

## 👤 Author

**Ahmed Ashraf**

[![GitHub](https://img.shields.io/badge/GitHub-ahmedashraf23413-181717?style=flat&logo=github)](https://github.com/ahmedashraf23413)

---

## 📄 License

This project is licensed under the **MIT License**.

---

⭐ **If you like this project, give it a star!**f
