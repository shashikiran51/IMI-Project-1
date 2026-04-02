import pandas as pd
import numpy as np

# Reproducibility
np.random.seed(42)

# Number of samples
n = 180

# -------------------------------
# SET 1: Polymer + Nanoparticle
# -------------------------------
polymer_types = ['PLGA', 'PLA', 'PEG', 'Chitosan']

set1 = pd.DataFrame({
    "Polymer_Type": np.random.choice(polymer_types, n),
    "Polymer_MW": np.random.uniform(10000, 100000, n),
    "Lactide_Glycolide_Ratio": np.random.choice([50, 65, 75, 85], n),
    "Polymer_Concentration": np.random.uniform(0.5, 5.0, n),
    "Polymer_Viscosity": np.random.uniform(0.1, 2.0, n),
    "Polymer_Density": np.random.uniform(1.0, 1.4, n),
    "Hydrophobicity_Index": np.random.uniform(0, 1, n),
    "Degradation_Rate": np.random.uniform(0.01, 0.2, n),
    "Particle_Size_nm": np.random.uniform(50, 300, n)
})

# Derived feature
set1["Surface_Area"] = 1000 / set1["Particle_Size_nm"]

# -------------------------------
# SET 2: Drug Features
# -------------------------------
drug_names = ['Doxorubicin', 'Ibuprofen', 'Paracetamol', 'Ciprofloxacin', 'Curcumin']
drug_classes = ['Anticancer', 'Analgesic', 'Antipyretic', 'Antibiotic', 'Natural']

set2 = pd.DataFrame({
    "Drug_Name": np.random.choice(drug_names, n),
    "Drug_MW": np.random.uniform(150, 600, n),
    "LogP": np.random.uniform(-1, 5, n),
    "Solubility": np.random.uniform(0.01, 10, n),
    "Polar_Surface_Area": np.random.uniform(20, 200, n),
    "H_Bond_Donors": np.random.randint(0, 6, n),
    "H_Bond_Acceptors": np.random.randint(1, 12, n),
    "Rotatable_Bonds": np.random.randint(0, 15, n),
    "pKa": np.random.uniform(2, 12, n),
    "Drug_Class": np.random.choice(drug_classes, n)
})

# -------------------------------
# SET 3: Process Features
# -------------------------------
solvents = ['Water', 'Ethanol', 'Acetone', 'DCM']
surfactants = ['PVA', 'Tween 80', 'Span 60', 'Pluronic F68']

set3 = pd.DataFrame({
    "pH": np.random.uniform(5.0, 8.0, n),
    "Temperature_C": np.random.uniform(20, 40, n),
    "Stirring_Speed_rpm": np.random.uniform(300, 1500, n),
    "Mixing_Time_min": np.random.uniform(10, 120, n),
    "Solvent_Type": np.random.choice(solvents, n),
    "Surfactant_Type": np.random.choice(surfactants, n),
    "Surfactant_Concentration": np.random.uniform(0.1, 2.0, n),
    "Organic_Aqueous_Ratio": np.random.uniform(0.1, 1.0, n),
    "Zeta_Potential_mV": np.random.uniform(-50, 50, n),
    "PDI": np.random.uniform(0.1, 0.5, n)
})

# -------------------------------
# COMBINE ALL SETS
# -------------------------------
final_df = pd.concat([set1, set2, set3], axis=1)

# Round values
final_df = final_df.round(3)

# Save to Excel
final_df.to_excel("Final_Dataset.xlsx", index=False)

# Preview
print(final_df.head())
