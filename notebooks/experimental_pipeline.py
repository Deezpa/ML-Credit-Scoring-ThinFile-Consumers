"""
Script: experimental_pipeline.py
Description: Experimental pipeline for credit scoring - from baseline model to fairness-aware evaluation
Author: Deepa Shukla
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, f1_score, confusion_matrix
from sklearn.preprocessing import StandardScaler, LabelEncoder

# Step 1: Load Dataset
df = pd.read_csv("../data/500Credit_Score_Dataset.csv")

# Step 2: Preprocessing
le_gender = LabelEncoder()
le_employment = LabelEncoder()
df['Gender'] = le_gender.fit_transform(df['Gender'])
df['Employment_Type'] = le_employment.fit_transform(df['Employment_Type'])

features = ['Loan_Defaults', 'Credit_Utilization', 'Mobile_Transactions',
            'Utility_Bill_Payment', 'Payment_History']
target = 'Credit_Score_Label'

scaler = StandardScaler()
df[features] = scaler.fit_transform(df[features])

# Step 3: Split
X = df[features]
y = df[target]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Step 4: Baseline Model
model = LogisticRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

# Step 5: Evaluation
print("Baseline Model Evaluation:")
print("Accuracy:", accuracy_score(y_test, y_pred))
print("F1 Score:", f1_score(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))

# Step 6: Optional Fairness Mitigation (requires AIF360, not included here for simplicity)
# Placeholder for bias mitigation methods
print("Fairness-aware enhancement is documented in the thesis, Figure 5.10.")
