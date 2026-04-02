import pandas as pd
import numpy as np

# Reproducibility
np.random.seed(42)

# Number of samples
n = 120   # >100 samples

# Drug names and classes
drug_names = ['Doxorubicin', 'Ibuprofen', 'Paracetamol', 'Ciprofloxacin', 'Curcumin']
drug_classes = ['Anticancer', 'Analgesic', 'Antipyretic', 'Antibiotic', 'Natural compound']

# Generate data
data = {
    "Drug_Name": np.random.choice(drug_names, n),

    "Drug_MW": np.random.uniform(150, 600, n),  # g/mol

    "LogP": np.random.uniform(-1, 5, n),

    "Solubility_mg_per_ml": np.random.uniform(0.01, 10, n),

    "Polar_Surface_Area": np.random.uniform(20, 200, n),

    "H_Bond_Donors": np.random.randint(0, 6, n),

    "H_Bond_Acceptors": np.random.randint(1, 12, n),

    "Rotatable_Bonds": np.random.randint(0, 15, n),

    "pKa": np.random.uniform(2, 12, n),

    "Drug_Class": np.random.choice(drug_classes, n)
}

# Create DataFrame
df = pd.DataFrame(data)

# Round values
df = df.round(3)

# Save to Excel
df.to_excel("Set_2_dataset.xlsx", index=False)

# Display first 5 rows
print(df.head())
