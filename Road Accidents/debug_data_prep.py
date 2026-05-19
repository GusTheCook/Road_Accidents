import pandas as pd
import glob
import os

base_path = r"C:\Users\guscr\OneDrive\Documents\Data Science Projects\Road Accidents"

def load_and_info(year):
    print(f"--- Loading {year} ---")
    files = {
        "caract": f"caract-{year}.csv",
        "lieux": f"lieux-{year}.csv",
        "usagers": f"usagers-{year}.csv",
        "vehicules": f"vehicules-{year}.csv"
    }
    
    data = {}
    for name, filename in files.items():
        path = os.path.join(base_path, filename)
        try:
            # Handling the known mixed type warning for lieux column 12 (1-based) -> index 11 or 12?
            # User said "Columns (12) have mixed types". Pandas warnings are 0-indexed usually? Or source was user text?
            # Let's inspect 'lieux' columns specifically.
            df = pd.read_csv(path, sep=";", encoding="utf-8", low_memory=False)
            data[name] = df
            print(f"{name}: shape={df.shape}")
            if name == 'lieux':
                 print(f"Lieux columns: {list(df.columns)}")
                 # Check column at index 12
                 if len(df.columns) > 12:
                     print(f"Column 12 (index 12): {df.columns[12]} dtype: {df.iloc[:, 12].dtype}")
                     
        except Exception as e:
            print(f"Error loading {filename}: {e}")
    return data

data_2023 = load_and_info(2023)
data_2024 = load_and_info(2024)

print("\n--- Verifying Consistency ---")
for key in data_2023:
    cols23 = set(data_2023[key].columns)
    cols24 = set(data_2024[key].columns)
    if cols23 != cols24:
        print(f"MISMATCH in {key} columns!")
        print(f"In 2023 but not 2024: {cols23 - cols24}")
        print(f"In 2024 but not 2023: {cols24 - cols23}")
    else:
        print(f"{key} columns match.")

print("\n--- Testing Merging Logic ---")
try:
    # Concatenate
    caract = pd.concat([data_2023['caract'], data_2024['caract']])
    lieux = pd.concat([data_2023['lieux'], data_2024['lieux']])
    usagers = pd.concat([data_2023['usagers'], data_2024['usagers']])
    vehicules = pd.concat([data_2023['vehicules'], data_2024['vehicules']])
    
    print(f"Combined shapes: caract={caract.shape}, lieux={lieux.shape}, usagers={usagers.shape}, vehicules={vehicules.shape}")
    
    # Merge test: Caract + Lieux
    merged_1 = pd.merge(caract, lieux, on='Num_Acc', how='inner')
    print(f"Merged Caract+Lieux: {merged_1.shape}")
    
except Exception as e:
    print(f"Merge error: {e}")
