Drift-Aware Utility-Optimized Credit Card Fraud Detection System
Project Overview

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

Utility-based decision optimization

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

System Architecture

The system replicates a realistic fraud detection lifecycle used in financial institutions:

Data exploration and behavioural analysis

Multi-model benchmarking

Champion model selection

Utility-based decision threshold optimization

Drift detection and monitoring

Explainable AI analysis

Real-time scoring API deployment

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
│
├── models
│   ├── lgbm_champion.pkl
│   └── lgbm_threshold.json
│
├── data
│   └── creditcard.csv
│
├── reports
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

Multiple machine learning models were trained and evaluated:

Logistic Regression

Random Forest

LightGBM

LightGBM was selected as the champion model due to its strong predictive performance and ability to maintain high fraud recall under strict false positive constraints.

2. Utility-Based Decision Optimization

Instead of optimizing the model using traditional metrics such as accuracy, the decision threshold is optimized based on business utility.

The optimization considers:

Fraud losses prevented

Operational costs of false positives

Customer experience impact

This ensures the fraud detection system maximizes financial value while maintaining a strict false positive rate constraint.

3. Drift Monitoring

Fraud behaviour evolves over time as attackers adapt to detection systems.

Without monitoring, model performance can deteriorate.

This system includes drift detection mechanisms such as:

Window-based performance monitoring

KL divergence distribution monitoring

Fraud recall degradation tracking

When drift is detected, retraining governance rules are triggered.

Explainability and Model Interpretation

Financial institutions must ensure fraud detection systems are transparent and auditable.

This project uses SHAP (SHapley Additive exPlanations) to explain how individual features influence model predictions.

Explainable AI supports:

Fraud analyst investigation

Model transparency

Regulatory compliance

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

{
  "fraud_probability": 0.00000008,
  "decision": "APPROVE"
}

This simulates how fraud detection models are integrated into live payment authorization systems used by banks and payment networks.

Running the API
Install Dependencies
pip install -r requirements.txt
Start the API Server
python -m uvicorn app:app --reload
Access Interactive API Documentation
http://127.0.0.1:8000/docs

The documentation interface allows users to test fraud scoring requests directly from the browser.

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

Feature store integration

Monitoring dashboards

Model governance and versioning

Author

Justine Chukwuemeka
MSc Business Analytics — Robert Gordon University
