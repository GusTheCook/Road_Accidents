import pandas as pd
import numpy as np
import os

base_path = r"C:\Users\guscr\OneDrive\Documents\Data Science Projects\Road Accidents"
os.chdir(base_path)

def load_year(year):
    print(f"Loading {year} data...")
    caract = pd.read_csv(f"caract-{year}.csv", sep=";", encoding="utf-8", low_memory=False)
    lieux = pd.read_csv(f"lieux-{year}.csv", sep=";", encoding="utf-8", low_memory=False)
    usagers = pd.read_csv(f"usagers-{year}.csv", sep=";", encoding="utf-8", low_memory=False)
    vehicules = pd.read_csv(f"vehicules-{year}.csv", sep=";", encoding="utf-8", low_memory=False)
    return caract, lieux, usagers, vehicules

try:
    c23, l23, u23, v23 = load_year(2023)
    c24, l24, u24, v24 = load_year(2024)

    # Concatenate
    caract = pd.concat([c23, c24], ignore_index=True)
    lieux = pd.concat([l23, l24], ignore_index=True)
    usagers = pd.concat([u23, u24], ignore_index=True)
    vehicules = pd.concat([v23, v24], ignore_index=True)

    # Clean Lieux types
    cols_to_fix = ['lartpc', 'larrout']
    for col in cols_to_fix:
        if col in lieux.columns:
            lieux[col] = pd.to_numeric(lieux[col], errors='coerce')

    # Dedup Lieux based on Num_Acc (keep first)
    lieux = lieux.drop_duplicates(subset=['Num_Acc'])

    # Create Target Variable
    def map_gravity(g):
        if g == 2: return 4 # Killed
        if g == 3: return 3 # Hospitalized
        if g == 4: return 2 # Light
        if g == 1: return 1 # Unhurt
        return 0

    usagers['severity_score'] = usagers['grav'].apply(map_gravity)
    accident_severity = usagers.groupby('Num_Acc')['severity_score'].max().reset_index()
    accident_severity.rename(columns={'severity_score': 'max_severity'}, inplace=True)
    
    severity_labels = {4: 'Fatal', 3: 'Serious', 2: 'Slight', 1: 'Unhurt', 0: 'Unknown'}
    accident_severity['severity_label'] = accident_severity['max_severity'].map(severity_labels)

    # Merge
    print("Merging datasets...")
    df_master = pd.merge(caract, lieux, on='Num_Acc', how='left')
    df_master = pd.merge(df_master, accident_severity, on='Num_Acc', how='left')

    # Save
    output_file = "road_accidents_consolidated.csv"
    df_master.to_csv(output_file, index=False)
    print(f"Successfully saved {output_file}. Shape: {df_master.shape}")

except Exception as e:
    print(f"An error occurred: {e}")
