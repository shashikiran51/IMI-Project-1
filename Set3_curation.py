import pandas as pd
import numpy as np

np.random.seed(42)  # so your data doesn't change every run

n = 40

# Base realistic ranges
age = np.random.randint(1, 365, n)
cement = np.random.uniform(200, 500, n)
water = np.random.uniform(120, 250, n)

temperature = np.random.uniform(10, 40, n)   # °C
humidity = np.random.uniform(30, 100, n)     # %

# Categorical options
exposure_conditions = ["Mild", "Moderate", "Severe"]
curing_types = ["Water Curing", "Steam Curing", "Air Curing"]
moisture_conditions = ["Dry", "Wet", "Saturated"]

# Create dataframe
df = pd.DataFrame({
    "Age": age,
    "Log_Age": np.log(age + 1),
    "Early_Age": (age <= 7).astype(int),
    "Cement_Age": cement * age,
    "Water_Age": water * age,
    "Temperature": temperature,
    "Humidity": humidity,
    "Exposure_Condition": np.random.choice(exposure_conditions, n),
    "Curing_Type": np.random.choice(curing_types, n),
    "Moisture_Condition": np.random.choice(moisture_conditions, n)
})

# Save to Excel
df.to_excel("set3_concrete_data.xlsx", index=False)

print("Dataset generated and saved as set3_concrete_data.xlsx")
