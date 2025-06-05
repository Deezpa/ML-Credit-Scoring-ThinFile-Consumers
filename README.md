# ML-Credit-Scoring-ThinFile-Consumers

🎓 Live Research Repository – PhD Thesis Implementation | Credit Scoring with ML & Fairness Evaluation
By Dr. Deepa Shukla, 2025
This repository presents the datasets, models, and fairness-aware algorithms developed as part of my PhD thesis.

> 📢 **Explore the live project site:**  
> 👉 [**ML-Credit-Scoring-ThinFile-Consumers GitHub Page**](https://deezpa.github.io/ML-Credit-Scoring-ThinFile-Consumers/)  
>  
> [![View Documentation](https://img.shields.io/badge/GitHub%20Pages-Visit%20Project%20Website-blue?logo=github)](https://deezpa.github.io/ML-Credit-Scoring-ThinFile-Consumers/)

 
# 📘 Machine Learning for Credit Scoring of Thin-File Consumers  
**Final PhD Thesis Implementation – Chapter 5**

[![DOI](https://zenodo.org/badge/DOI/10.7910/DVN/6MLVVI.svg)](https://doi.org/10.7910/DVN/6MLVVI)  
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)  
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Deezpa/ML-Credit-Scoring-ThinFile-Consumers/blob/main/notebooks/thesis_demo_colab.ipynb)

---

## 🎓 Project Overview

This repository contains the complete implementation of Chapter 5 of my PhD thesis, titled:  
**"Machine Learning Algorithms for Credit Scoring of Thin-File Consumers: A Fairness-Aware Evaluation"**

It addresses the challenge of evaluating creditworthiness for **thin-file consumers**—individuals with limited or no traditional credit history—using machine learning models, **alternative data**, and **fairness-aware methodologies**.

---
ML-Credit-Scoring-ThinFile-Consumers/
│
├── notebooks/ # Jupyter notebooks: training, SHAP/LIME, fairness
├── results/ # Visualizations, model outputs, fairness plots
├── tables/ # Tables 5.1–5.6 in CSV format
├── thesis_demo_colab.ipynb# Google Colab-compatible demo
├── LICENSE # MIT License
├── README.md # You’re here
├── CITATION.cff # Citation metadata


---

## 📊 Dataset

A synthetic dataset was created and published as part of this thesis to support reproducibility and fairness research:

📘 **Dataset Title**: *Synthetic Credit Score of Thin-File Consumers*  
📅 **Published**: May 2024  
📁 **Hosted on**: [Harvard Dataverse](https://dataverse.harvard.edu/)  
🔗 **Permanent DOI**: [https://doi.org/10.7910/DVN/6MLVVI](https://doi.org/10.7910/DVN/6MLVVI)
**📂 Format:** CSV with metadata following FAIR principles  
**🔍 Contents:** Credit scoring features (traditional + alternative), synthetic labels, demographic proxies

### 📚 Citation

If you use this dataset in your research, please cite as:

```bibtex
@dataset{shukla_2024_synthetic,
  author       = {Deepa Shukla},
  title        = {Synthetic Credit Score of Thin-File Consumers},
  year         = 2024,
  doi          = {10.7910/DVN/6MLVVI},
  url          = {https://doi.org/10.7910/DVN/6MLVVI}
}

---

## 🧠 Models Implemented

| Model                     | Description                              |
|--------------------------|------------------------------------------|
| Logistic Regression       | Linear baseline                          |
| Decision Tree             | Interpretable tree-based learner         |
| Random Forest             | Ensemble method for robust performance   |
| Gradient Boosting         | Fine-grained boosting classifier         |
| Support Vector Machine    | Margin-based nonlinear classifier        |
| Deep Neural Network (DNN) | Multi-layer perceptron-based classifier  |

---

## ⚖️ Fairness-Aware Evaluation

This work integrates fairness into machine learning model evaluation through:

- Bias Mitigation Pipelines  
- Pre/Post Fairness Score Comparison  
- Fairness–Accuracy Tradeoff Visualizations  
- SHAP & LIME Interpretability Tools

---

## 🗂️ Repository Structure


---

## 📈 Results Summary (Thesis Chapter 5)

| Table No. | Description                                                |
|-----------|------------------------------------------------------------|
| 5.1       | AUC-ROC Scores for Traditional Models                      |
| 5.2       | Performance on Alternative Data Features                   |
| 5.3       | Model Comparison (AUC, F1)                                 |
| 5.4       | Fairness Metrics across Models                             |
| 5.5       | Bias Scores (Before vs After Mitigation)                  |
| 5.6       | Fairness-aware Model Performance (AUC, Bias %)            |

All tables are reproducible via linked notebooks and available in `/tables/`.

---

## 📚 How to Cite

Please cite this repository and dataset using the following format:

```bibtex
@dataset{shukla_2024_synthetic,
  author       = {Deepa Shukla},
  title        = {Synthetic Credit Score of Thin-File Consumers},
  year         = 2024,
  doi          = {10.7910/DVN/6MLVVI},
  url          = {https://doi.org/10.7910/DVN/6MLVVI}
}

@misc{shukla_2025_repo,
  author       = {Deepa Shukla},
  title        = {ML-Credit-Scoring-ThinFile-Consumers},
  year         = 2025,
  howpublished = {\url{https://github.com/Deezpa/ML-Credit-Scoring-ThinFile-Consumers}},
  note         = {Version 1.0 – Final Thesis Implementation}
}
