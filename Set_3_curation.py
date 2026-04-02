import pandas as pd
import numpy as np

# Reproducibility
np.random.seed(42)

# Number of samples
n = 120   # >100 samples

# Categories
solvents = ['Water', 'Ethanol', 'Acetone', 'Dichloromethane']
surfactants = ['PVA', 'Tween 80', 'Span 60', 'Pluronic F68']

# Generate data
data = {
    "pH": np.random.uniform(5.0, 8.0, n),

    "Temperature_C": np.random.uniform(20, 40, n),

    "Stirring_Speed_rpm": np.random.uniform(300, 1500, n),

    "Mixing_Time_min": np.random.uniform(10, 120, n),

    "Solvent_Type": np.random.choice(solvents, n),

    "Surfactant_Type": np.random.choice(surfactants, n),

    "Surfactant_Concentration_%": np.random.uniform(0.1, 2.0, n),

    "Organic_Aqueous_Ratio": np.random.uniform(0.1, 1.0, n),

    "Zeta_Potential_mV": np.random.uniform(-50, 50, n),

    "PDI": np.random.uniform(0.1, 0.5, n)
}

# Create DataFrame
df = pd.DataFrame(data)

# Round values
df = df.round(3)

# Save to Excel
df.to_excel("Set_3_dataset.xlsx", index=False)

# Display first 5 rows
print(df.head())
