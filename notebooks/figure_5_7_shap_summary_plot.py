import pandas as pd
import shap
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler

# Load dataset
df = pd.read_csv("../data/500Credit_Score_Dataset.csv")

# Encode categorical variables
df['Gender'] = LabelEncoder().fit_transform(df['Gender'])
df['Employment_Type'] = LabelEncoder().fit_transform(df['Employment_Type'])

# Selected features (Figure 5.7)
features = ['Loan_Defaults', 'Credit_Utilization', 'Mobile_Transactions',
            'Utility_Bill_Payment', 'Payment_History']
target = 'Credit_Score_Label'

# Normalize feature values
df[features] = StandardScaler().fit_transform(df[features])

# Split into train and test
X = df[features]
y = df[target]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Train Logistic Regression
model = LogisticRegression()
model.fit(X_train, y_train)

# SHAP explanation
explainer = shap.Explainer(model.predict, X_train)
shap_values = explainer(X_test)

# SHAP summary plot
shap.summary_plot(shap_values, X_test, show=True, plot_size=(9, 5))
