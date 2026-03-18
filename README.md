# Drift-Aware Utility-Optimized Credit Card Fraud Detection System

---

## 1. Project Overview

This project presents a **production-oriented fraud detection system** designed for financial institutions, integrating **machine learning, business cost optimization, and model monitoring**.

Unlike traditional approaches that focus solely on accuracy, this system incorporates:
- **Concept drift awareness** to maintain performance over time  
- **Utility-based optimization** to align decisions with business cost  
- **Explainability and monitoring** for transparency and governance  

The solution reflects how modern banks design fraud detection systems that are **robust, adaptive, and business-aligned**.

---

## 2. Business Problem

Credit card fraud remains a major challenge in financial services due to:

- **Highly imbalanced data** (fraud cases are rare but costly)  
- **Evolving fraud patterns (concept drift)** that degrade model performance  
- **Trade-offs between detection and customer experience**  

Traditional systems:
- Focus on accuracy instead of **business cost impact**  
- Do not adapt to **changing fraud behavior**  
- Lack **monitoring and governance frameworks**  

---

## 3. Objectives

- Build a **robust fraud detection model** for imbalanced data  
- Implement **drift-aware monitoring** to track performance over time  
- Optimize decision-making using **cost-sensitive thresholds**  
- Provide **model explainability (SHAP)** for transparency  
- Simulate a **real-world deployment pipeline** via API  

---

## 4. Methodology

### Data
- Credit card transaction dataset  
- Highly imbalanced fraud vs non-fraud distribution  
- Anonymized features for privacy  

### Approach

#### Model Development
Three models were trained and evaluated:
- Logistic Regression (baseline)  
- Random Forest (ensemble model)  
- LightGBM (gradient boosting – selected champion)  

#### Utility Optimization
- Decision threshold optimized based on:
  - Cost of missed fraud (false negatives)  
  - Cost of false alerts (false positives)  

#### Drift Monitoring
- **KL-Divergence** for distribution shift detection  
- **Recall monitoring across time windows** for performance stability  

#### Explainability
- **SHAP** used to identify key fraud drivers and support interpretability  

#### Deployment
- **FastAPI** endpoint for real-time transaction scoring  

---

## 5. System Architecture


Data → Feature Engineering → Model Training → Threshold Optimization
→ Drift Monitoring → Explainability → API Scoring → Reporting


---

## 6. Results & Performance

Three models were evaluated to determine the most effective solution.

### Model Comparison

| Model                | ROC-AUC | Precision | Recall (Fraud) | F1 Score | False Positive Rate | Business Interpretation |
|---------------------|--------|----------|----------------|----------|---------------------|-------------------------|
| Logistic Regression | 0.91   | 0.65     | 0.70           | 0.67     | Low                 | Misses significant fraud due to inability to capture complex patterns |
| Random Forest       | 0.94   | 0.73     | 0.79           | 0.76     | Moderate            | Better detection but increases false positives |
| LightGBM (Champion) | 0.9655 | 0.77     | 0.8378         | 0.80     | Very Low (0.0042)   | Best balance between fraud detection and operational efficiency |

---

### Interpretation

- Logistic Regression serves as a baseline but underperforms in fraud detection  
- Random Forest improves detection but increases operational burden  
- LightGBM delivers:
  - **Highest fraud detection rate (83.78%)**  
  - **Very low false positive rate (0.42%)**  
  - **Optimal balance between risk and customer experience**  

---

### Champion Model Achievement (LightGBM)

The selected model successfully achieves:

- Strong fraud detection under **extreme class imbalance**  
- Alignment with **cost-sensitive business decisions**  
- Stability under **data drift through monitoring integration**  
- Compatibility with **explainability (SHAP)**  
- Readiness for **real-time deployment via API**  

---

## 7. Key Insights

- Fraud detection performance degrades without monitoring  
- Drift-aware systems maintain **stable performance over time**  
- Threshold optimization significantly reduces **false positive impact**  
- Small improvements in recall lead to **significant cost savings**  
- Explainability enhances **trust and regulatory compliance**  

---

## 8. Business Value & Implications

This system provides:

- **Reduced fraud losses** through improved detection  
- **Lower operational costs** from fewer false alerts  
- **Improved customer experience** by minimizing transaction disruptions  
- **Regulatory compliance** via explainable AI  
- **Scalable deployment capability** for real-time fraud detection  

---

## 9. Limitations

- Anonymized dataset limits business-specific interpretation  
- Drift simulation may not fully reflect real-world dynamics  
- API is deployed locally (not cloud-based)  
- Model performance depends on data refresh frequency  

---

## 10. Future Work

- Real-time streaming deployment (Kafka, cloud platforms)  
- Advanced drift detection methods (ADWIN, DDM)  
- Automated retraining pipelines  
- Integration with fraud investigation workflows  
- Dashboard development (Power BI / Streamlit)  

---

## 11. Technologies Used

- Python  
- Pandas, NumPy  
- Scikit-learn  
- LightGBM  
- SHAP  
- Matplotlib, Seaborn  
- FastAPI, Uvicorn  
- Joblib  

---

## 12. How to Run the Project

### Clone repository
```bash
git clone https://github.com/Justine-N/fraud-detection-ml-system.git
cd fraud-detection-ml-system
Install dependencies
pip install -r requirements.txt
Run notebooks

Execute in order:

Data exploration

Model training

Utility optimization

Drift monitoring

Run API
uvicorn app:app --reload
Access API
http://127.0.0.1:8000/docs
Conclusion

This project delivers a drift-aware, cost-optimized fraud detection system aligned with real-world banking needs.

The champion LightGBM model achieved:

High fraud detection (~83.78%), reducing financial losses

Low false positive rate (~0.42%), preserving customer experience

Cost-sensitive optimization, balancing fraud loss and operational cost

Sustained performance under drift, enabling proactive monitoring and retraining

Business Impact

Reduced fraud losses

Lower operational investigation costs

Improved customer trust and retention

Enhanced regulatory transparency

Scalable real-time fraud detection capability

Final Remark

This system demonstrates how machine learning can move beyond prediction to deliver measurable business value, combining detection performance, cost efficiency, and operational resilience in modern fraud prevention systems.
