
import pandas as pd
import numpy as np

np.random.seed(42)

n_patients = 5000
patients = pd.DataFrame({
    'patient_id': range(1, n_patients+1),
    'age': np.random.randint(18, 90, n_patients),
    'sex': np.random.choice(['Male','Female'], n_patients),
    'smoker': np.random.choice([0,1], n_patients, p=[0.7,0.3])
})

visits = pd.DataFrame({
    'patient_id': np.random.choice(patients['patient_id'], n_patients*3),
    'year': np.random.choice(range(2018,2024), n_patients*3),
    'systolic_bp': np.random.normal(120,15,n_patients*3).astype(int),
    'diastolic_bp': np.random.normal(80,10,n_patients*3).astype(int)
})

patients.to_csv('../data/raw/patients.csv', index=False)
visits.to_csv('../data/raw/visits.csv', index=False)
