# Drift-Aware Utility-Optimized Credit Card Fraud Detection System


This project implements a production-inspired credit card fraud detection system designed to balance fraud detection performance, customer experience, and business cost constraints.

Many fraud detection projects focus purely on model accuracy. However, real financial institutions must consider additional operational constraints such as:

Customer disruption caused by false positives

Financial loss from undetected fraud

Regulatory requirements for explainability

Model performance degradation over time

Real-time decision requirements

This project simulates how banks and financial institutions design, deploy, and maintain fraud detection systems by integrating predictive modelling with decision optimization, monitoring, explainability, and real-time scoring.

The goal is to demonstrate a complete machine learning lifecycle, from model development to production deployment and monitoring.

Business Problem

Credit card fraud is a major operational risk for financial institutions. Banks process millions of transactions daily, and even a small fraud detection failure rate can result in significant financial loss.

However, fraud detection systems must balance two competing objectives:

Detect as many fraudulent transactions as possible

Avoid blocking legitimate customer transactions

Excessive false positives lead to:

Customer frustration

Lost revenue

Increased operational costs for manual reviews

Therefore, fraud detection systems must optimize decisions based on business utility, rather than purely statistical metrics.

This project simulates a bank-grade fraud detection strategy by implementing:

Predictive fraud modelling

## Project Overview

This project implements a **production-inspired credit card fraud detection system** designed to balance **fraud detection performance, customer experience, and business cost constraints**.

Many fraud detection projects focus purely on model accuracy. However, real financial institutions must consider additional operational constraints such as:
 (Update README with portfolio positioning)

- Customer disruption caused by false positives  
- Financial loss from undetected fraud  
- Regulatory requirements for explainability  
- Model performance degradation over time  
- Real-time decision requirements  


Drift monitoring for model degradation

Explainable AI for transparency

Real-time fraud scoring infrastructure

Key Results
Metric	Result
ROC-AUC	0.9655
PR-AUC	0.8385
Fraud Recall @ 0.2% FPR	83.78%
Customer Approval Rate	99.81%
Estimated Business Utility	£5,965

These results demonstrate that the model detects a high proportion of fraudulent transactions while maintaining a very low false positive rate, ensuring minimal disruption to legitimate customers.

This project simulates how **banks and financial institutions design, deploy, and maintain fraud detection systems** by integrating predictive modelling with decision optimization, monitoring, explainability, and real-time scoring.

The goal is to demonstrate a **complete machine learning lifecycle**, from model development to production deployment and monitoring.



## Business Problem

Credit card fraud is a major operational risk for financial institutions. Banks process **millions of transactions daily**, and even a small fraud detection failure rate can result in significant financial loss.

However, fraud detection systems must balance **two competing objectives**:

1. Detect as many fraudulent transactions as possible  
2. Avoid blocking legitimate customer transactions  

Excessive false positives lead to:

- Customer frustration  
- Lost revenue  
- Increased operational costs for manual reviews  

Therefore, fraud detection systems must optimize decisions based on **business utility**, rather than purely statistical metrics.

This project simulates a **bank-grade fraud detection strategy** by implementing:
 (Update README with portfolio positioning)

- Predictive fraud modelling  
- Utility-based decision optimization  
- Drift monitoring for model degradation  
- Explainable AI for transparency  
- Real-time fraud scoring infrastructure  


The system replicates a realistic fraud detection lifecycle used in financial institutions:

Data exploration and behavioural analysis
=======
---

## Key Results (Update README with portfolio positioning)

| Metric | Result |
|--------|--------|
| ROC-AUC | 0.9655 |
| PR-AUC | 0.8385 |
| Fraud Recall @ 0.2% FPR | 83.78% |
| Customer Approval Rate | 99.81% |
| Estimated Business Utility | £5,965 |

These results demonstrate that the model detects a **high proportion of fraudulent transactions while maintaining a very low false positive rate**, ensuring minimal disruption to legitimate customers.


Utility-based decision threshold optimization

Drift detection and monitoring

Explainable AI analysis


## System Architecture

The system replicates a **realistic fraud detection lifecycle used in financial institutions**:

1. Data exploration and behavioural analysis  
2. Multi-model benchmarking  
3. Champion model selection  
4. Utility-based decision threshold optimization  
5. Drift detection and monitoring  
6. Explainable AI analysis  
7. Real-time scoring API deployment  

### Architecture Diagram

![Fraud Detection Architecture](images/architecture.png)

The architecture illustrates the **end-to-end fraud detection pipeline**, including:

- Feature engineering  
- Model training  
- Fraud probability scoring  
- Decision threshold optimisation  
- Monitoring and drift detection  
- Automated retraining triggers  

---

## Project Structure
(Update README with portfolio positioning)



Architecture Diagram

The architecture illustrates the end-to-end fraud detection pipeline, including:

Feature engineering

Model training

Fraud probability scoring

Decision threshold optimisation

Monitoring and drift detection

Automated retraining triggers

Project Structure
fraud-detection-ml-system
│
├── notebooks
│   ├── 01_data_exploration.ipynb
│   ├── 02_model_training.ipynb
│   ├── 03_utility_optimization.ipynb
│   ├── 04_drift_simulation.ipynb
│   └── 05_monitoring.ipynb
=======
fraud-detection-ml-system
│
├── notebooks
│ ├── 01_data_exploration.ipynb
│ ├── 02_model_training.ipynb
│ ├── 03_utility_optimization.ipynb
│ ├── 04_drift_simulation.ipynb
│ └── 05_monitoring.ipynb
 (Update README with portfolio positioning)
│
├── models
│ ├── lgbm_champion.pkl
│ └── lgbm_threshold.json
│
├── data
│ └── creditcard.csv
│
├── images
│ ├── architecture.png
│ ├── shap_summary.png
│ └── confusion_matrix.png
│
├── app.py
├── requirements.txt
└── README.md

Key Features Used by the Model

Fraud detection models rely heavily on transaction behaviour patterns rather than individual features.

The model incorporates several engineered features designed to capture suspicious activity patterns.

Feature Category	Description
Transaction Amount	Value of the transaction being processed
Transaction Time	Time-based patterns that may indicate abnormal behaviour
Account Behaviour	Historical transaction behaviour for the account
Balance Changes	Differences between previous and current account balances
Destination Behaviour	Frequency of transactions to specific recipients
Transaction Velocity	Number of transactions within short time windows

These behavioural indicators help the model detect patterns such as:

Rapid transaction bursts

Unusual transaction sizes

Suspicious balance changes

Transfers to unfamiliar accounts

Feature engineering plays a critical role in improving fraud detection performance and model robustness.

Machine Learning Pipeline
1. Predictive Modelling

 (Update README with portfolio positioning)


---

## Key Features Used by the Model

Fraud detection models rely heavily on **transaction behaviour patterns** rather than individual variables.

LightGBM was selected as the champion model due to its strong predictive performance and ability to maintain high fraud recall under strict false positive constraints.

2. Utility-Based Decision Optimization

Instead of optimizing the model using traditional metrics such as accuracy, the decision threshold is optimized based on business utility.

The optimization considers:

Fraud losses prevented

Operational costs of false positives

Customer experience impact

This ensures the fraud detection system maximizes financial value while maintaining a strict false positive rate constraint.
=======
| Feature Category | Description |
|----------------|-------------|
| Transaction Amount | Value of the transaction |
| Transaction Time | Time-based behaviour patterns |
| Account Behaviour | Historical activity patterns |
| Balance Changes | Differences before and after transactions |
| Destination Behaviour | Frequency of transfers to recipients |
| Transaction Velocity | Number of transactions within short time windows |

These features help detect patterns such as:

- Rapid transaction bursts  
- Unusual transaction sizes  
- Suspicious balance changes  
- Transfers to unfamiliar accounts  



## Machine Learning Pipeline

### 1. Predictive Modelling

Models trained and evaluated:
 (Update README with portfolio positioning)

- Logistic Regression  
- Random Forest  
- LightGBM  


Fraud behaviour evolves over time as attackers adapt to detection systems.

Without monitoring, model performance can deteriorate.

This system includes drift detection mechanisms such as:

LightGBM was selected as the **champion model** due to its strong performance and ability to maintain **high fraud recall under strict false positive constraints**.


(Update README with portfolio positioning)

### 2. Utility-Based Decision Optimization


KL divergence distribution monitoring

Fraud recall degradation tracking

Instead of optimizing for traditional metrics such as accuracy, the system optimizes **business utility**.

This considers:
(Update README with portfolio positioning)

- Fraud loss prevention  
- Cost of false positives  
- Customer experience impact  


Explainability and Model Interpretation

Financial institutions must ensure fraud detection systems are transparent and auditable.

This project uses SHAP (SHapley Additive exPlanations) to explain how individual features influence model predictions.

Explainable AI supports:

Fraud analyst investigation



### 3. Drift Monitoring

Fraud behaviour evolves over time.

Monitoring techniques include:
(Update README with portfolio positioning)

- Window-based performance tracking  
- KL divergence  
- Recall drop detection  

Retraining is triggered when performance degrades.


Improved stakeholder trust

SHAP analysis identifies which transaction characteristics most strongly contribute to fraud predictions, helping analysts understand the model’s decision logic.

Typical influential features include:

Transaction amount anomalies

Rapid transaction frequency

Suspicious balance transitions

Unusual destination account behaviour

Real-Time Fraud Scoring API

The trained model is deployed using FastAPI, enabling real-time scoring of incoming transactions.

Example API response:


## Explainability and Model Interpretation

The model uses **SHAP (SHapley Additive exPlanations)** to interpret predictions.
(Update README with portfolio positioning)

### SHAP Summary Plot

![SHAP Summary](images/shap_summary.png)

Explainability supports:

- Fraud analyst investigation  
- Model transparency  
- Regulatory compliance  

Key drivers of fraud predictions include:

- Transaction amount anomalies  
- High transaction frequency  
- Balance inconsistencies  
- Suspicious destination accounts  


## Real-Time Fraud Scoring API

The model is deployed using **FastAPI** for real-time transaction scoring.

### Example Response

```json
{
  "fraud_probability": 0.00000008,
  "decision": "APPROVE"
}

This simulates how fraud detection models are integrated into live payment authorization systems used by banks and payment networks.

Running the API
Install Dependencies
pip install -r requirements.txt
<<<<<<< HEAD
Start the API Server
python -m uvicorn app:app --reload
Access Interactive API Documentation
http://127.0.0.1:8000/docs

The documentation interface allows users to test fraud scoring requests directly from the browser.

Start Server
python -m uvicorn app:app --reload
API Docs
http://127.0.0.1:8000/docs
(Update README with portfolio positioning)
Tools and Technologies

Python

Scikit-Learn

LightGBM

SHAP

FastAPI

Pandas

NumPy

Matplotlib / Seaborn

Future Improvements

Potential enhancements include:

Real-time streaming fraud detection pipelines

Automated model retraining pipelines
Real-time streaming pipelines

Automated retraining
 (Update README with portfolio positioning)

Feature store integration

Monitoring dashboards

Model governance and versioning

Author

Justine Chukwuemeka

MSc Business Analytics — Robert Gordon University
MSc Business Analytics — Robert Gordon University
(Update README with portfolio positioning)
