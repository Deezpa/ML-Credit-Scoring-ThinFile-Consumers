# Thesis Overview: Machine Learning Algorithms for Credit Scoring of Thin-File Consumers

## 🎯 Research Objectives
- To develop robust machine learning-based credit scoring models tailored to **thin-file consumers**.
- To incorporate **alternative datasets** (e.g., digital footprints, psychometric indicators) for improving creditworthiness predictions.
- To enhance **fairness**, **transparency**, and **performance** of credit scoring through algorithmic improvements and explainability.

## 🧪 Methodology Summary
The research follows a structured four-phase approach:

1. **Data Collection**
   - Traditional features: age, income, credit history
   - Alternative features: utility bill payments, mobile transaction frequency, employment pattern
   - A **synthetic dataset** was generated and validated using realistic distributions

2. **Model Development**
   - Machine learning models: Logistic Regression, Decision Tree, Random Forest, Gradient Boosting, Support Vector Machine, Deep Neural Networks
   - Bias mitigation methods: preprocessing (reweighting), in-processing (fair classifiers), and post-processing

3. **Evaluation**
   - Metrics: Accuracy, AUC-ROC, Precision, Recall, F1-Score
   - Fairness indicators: Demographic Parity, Equal Opportunity, Bias Reduction %

4. **Model Explanation**
   - Global and local interpretability: SHAP for overall feature importance, LIME for individual predictions

## 📌 Key Findings
- Models using **alternative data** outperformed traditional-only approaches by up to **6% AUC gain**.
- **Fairness-aware models** showed a **35–40% reduction in bias** without significant performance degradation.
- SHAP analysis revealed that **mobile transactions**, **payment history**, and **utility bill patterns** were among the most influential predictors.
- LIME explanations demonstrated the potential for **transparent and auditable decisions**, crucial for inclusive credit systems.

---

**Author**: Deepa Shukla  
**Institution**: Jaipur National University  
**Repository**: [ML-Credit-Scoring-ThinFile-Consumers](https://github.com/Deezpa/ML-Credit-Scoring-ThinFile-Consumers)
