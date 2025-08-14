
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import json

df = pd.read_csv('../data/processed/merged_data.csv')

# KPI calculation
kpis = {
    'average_systolic': df['systolic_bp'].mean(),
    'average_diastolic': df['diastolic_bp'].mean(),
    'smoker_percentage': (df['smoker'].sum()/len(df))*100
}
pd.DataFrame([kpis]).to_csv('../reports/kpis.csv', index=False)

# Simple logistic regression: predict smoker status by BP & age
X = df[['systolic_bp','diastolic_bp','age']]
y = df['smoker']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LogisticRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

metrics = {'accuracy': accuracy_score(y_test, y_pred)}
with open('../reports/model_metrics.json','w') as f:
    json.dump(metrics, f)
