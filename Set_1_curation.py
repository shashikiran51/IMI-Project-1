import pandas as pd
import numpy as np

# Reproducibility
np.random.seed(42)

# Number of samples
n = 120   # >100 samples

# Polymer types
polymer_types = ['PLGA', 'PLA', 'PEG', 'Chitosan']

# Generate data
data = {
    "Polymer_Type": np.random.choice(polymer_types, n),

    "Polymer_MW": np.random.uniform(10000, 100000, n),  # g/mol

    "Lactide_Glycolide_Ratio": np.random.choice([50, 65, 75, 85], n),

    "Polymer_Concentration": np.random.uniform(0.5, 5.0, n),  # %

    "Polymer_Viscosity": np.random.uniform(0.1, 2.0, n),  # Pa.s

    "Polymer_Density": np.random.uniform(1.0, 1.4, n),  # g/cm³

    "Hydrophobicity_Index": np.random.uniform(0, 1, n),

    "Degradation_Rate": np.random.uniform(0.01, 0.2, n),  # per day

    "Particle_Size_nm": np.random.uniform(50, 300, n)
}

# Create DataFrame
df = pd.DataFrame(data)

# Derived Feature: Surface Area
df["Surface_Area"] = 1000 / df["Particle_Size_nm"]

# Round values
df = df.round(3)

# Save to Excel
df.to_excel("Set_1_dataset.xlsx", index=False)

# Display first 5 rows
print(df.head())
