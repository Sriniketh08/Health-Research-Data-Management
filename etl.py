
import pandas as pd
import sqlite3

patients = pd.read_csv('../data/raw/patients.csv')
visits = pd.read_csv('../data/raw/visits.csv')

# Merge data
df = visits.merge(patients, on='patient_id')

# Save processed CSV
df.to_csv('../data/processed/merged_data.csv', index=False)

# Load into SQLite
conn = sqlite3.connect('../db/research.db')
df.to_sql('patients', conn, if_exists='replace', index=False)
conn.close()
