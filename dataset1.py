import pandas as pd
import numpy as np

np.random.seed(42)

n = 100

# Base composition ranges (realistic)
cement = np.random.uniform(200, 500, n)
slag = np.random.uniform(0, 200, n)
fly_ash = np.random.uniform(0, 150, n)
water = np.random.uniform(120, 250, n)
superplasticizer = np.random.uniform(0, 25, n)

coarse_agg = np.random.uniform(800, 1200, n)
fine_agg = np.random.uniform(600, 1000, n)

# Derived features
binder = cement + slag + fly_ash

water_cement_ratio = water / cement
water_binder_ratio = water / (binder + 1)  # avoid divide by zero

# Create dataframe
df = pd.DataFrame({
    "Cement": cement,
    "Blast_Furnace_Slag": slag,
    "Fly_Ash": fly_ash,
    "Water": water,
    "Superplasticizer": superplasticizer,
    "Coarse_Aggregate": coarse_agg,
    "Fine_Aggregate": fine_agg,
    "Binder_Content": binder,
    "Water_Cement_Ratio": water_cement_ratio,
    "Water_Binder_Ratio": water_binder_ratio
})

# Save to Excel
df.to_excel("set1_concrete_data.xlsx", index=False)

print("Dataset generated and saved as set1_concrete_data.xlsx")
