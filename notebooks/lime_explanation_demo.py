import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
import lime
import lime.lime_tabular

# Load dataset
df = pd.read_csv("../data/500Credit_Score_Dataset.csv")

# Encode categorical features
df['Gender'] = LabelEncoder().fit_transform(df['Gender'])
df['Employment_Type'] = LabelEncoder().fit_transform(df['Employment_Type'])

# Select thesis-based features
features = ['Loan_Defaults', 'Credit_Utilization', 'Mobile_Transactions',
            'Utility_Bill_Payment', 'Payment_History']
target = 'Credit_Score_Label'

# Normalize feature values
scaler = StandardScaler()
df[features] = scaler.fit_transform(df[features])

# Define features and target
X = df[features].values
y = df[target].values

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)

# Fit logistic regression model
model = LogisticRegression()
model.fit(X_train, y_train)

# LIME explainer
explainer = lime.lime_tabular.LimeTabularExplainer(
    training_data=X_train,
    feature_names=features,
    class_names=['Bad Risk', 'Good Risk'],
    mode='classification'
)

# Pick a sample instance to explain
i = 7  # Any test sample index
exp = explainer.explain_instance(X_test[i], model.predict_proba, num_features=5)

# Visualize explanation
exp.show_in_notebook(show_table=True)
fig = exp.as_pyplot_figure()
plt.tight_layout()
plt.title("LIME Explanation for One Prediction (Figure 5.8)")
plt.show()
