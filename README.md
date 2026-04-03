---

# 🔥 Bank Loan Approval Prediction System

A **production-ready Machine Learning web application** that predicts whether a loan should be **Approved or Rejected** based on applicant data.

Deployed fully on **Vercel (Frontend + Backend)** with a modular and scalable architecture.

---

## 📌 🚀 Live Demo

***[(Live Demo)](https://bank-loan-approval-prediction-nine.vercel.app/)***

---

## 🧠 Problem Statement

Financial institutions receive thousands of loan applications daily.
This system automates decision-making using Machine Learning to:

* Reduce manual effort
* Improve consistency
* Speed up approval process

---

## ⚙️ Tech Stack

### 💻 Frontend

* HTML, CSS, JavaScript
* Responsive UI
* Form-based input system

### 🧠 Backend

* Python (Flask)
* REST API (`/predict` endpoint)

### 🤖 Machine Learning

* Scikit-learn
* Pandas, NumPy
* Model serialization using Pickle

### ☁️ Deployment

* **Vercel (Full-stack deployment)**

---

## 📂 Project Structure

```
.
├── .vercel/                         # Vercel deployment config
├── logs/                            # Application logs
├── templates/                       # HTML templates
├── artifact/                        # Saved ML models & files
├── src/
│   ├── components/                  # ML components (training, preprocessing)
│   ├── pipeline/                    # Prediction pipeline
├── notebook/                        # Jupyter notebooks (EDA, training)
├── venv/                            # Virtual environment (ignored)
├── Bank_Loan_Approval_Prediction.egg-info
├── .git/                            # Git version control
```

---

## 🔄 Application Flow

1. User enters loan details via UI
2. Data is sent to `/predict` API
3. Backend processes input using trained model
4. Prediction is returned:

   * ✅ Approved
   * ❌ Rejected

---

## 🧪 Features

* Clean UI for user input
* Real-time prediction
* Modular ML pipeline
* Logging system for debugging
* Scalable backend structure
* Fully deployed on cloud (Vercel)

---

## 📊 Model Pipeline

* Data Cleaning
* Feature Engineering
* Model Training
* Model Serialization
* Prediction Pipeline

---

## 🛠️ Installation (Local Setup)

```bash
# Clone repository
git clone https://github.com/suvancodes/loan-approval-predictor.git

# Navigate to project
cd loan-approval-predictor

# Create conda environment
conda create -n loan-env python=3.10 -y

# Activate environment
conda activate loan-env

# Install dependencies
pip install -r requirements.txt

# Run application
python app.py
```

---

## 🌐 API Endpoint

### `/predict`

**Method:** POST

**Input:** JSON / Form Data
**Output:** Loan Status

---

## 📈 Logs

All system logs are stored in:

```
/logs/
```

Useful for:

* Debugging
* Monitoring model behavior

---

## ⚠️ Important Notes (Real Talk)

I’m going to be brutally honest here 👇

Right now your project is **good**, but not yet *top-tier industry level*. To truly stand out, you should add:

### 🔥 Must Add Next:

* Input validation (very important)
* Model accuracy + metrics in README
* Screenshot / UI preview
* Error handling (bad input cases)
* Docker support (huge plus for recruiters)
* CI/CD pipeline (GitHub Actions)

---

## 💡 Future Improvements

* Add authentication system
* Store prediction history (DB)
* Improve UI (React upgrade)
* Add explainability (SHAP / LIME)
* Deploy model separately as microservice

---

## 👨‍💻 Author

**Suvankar Payra 👉 *[(suvancodes)](https://github.com/suvancodes)***

Aspiring AI/ML Engineer 🚀

---
