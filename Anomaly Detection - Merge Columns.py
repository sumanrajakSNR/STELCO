#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os

import pandas as pd

# Paths
master_csv = "coil_anomaly_volatility_phasewise_good.csv"
coil_folder = r"D:\Stelco\Work\Dynamic Correlation\Key\Whole_Phase_Good_Clustered"

# Load master file
master_df = pd.read_csv(master_csv)

# Extract unique coil IDs
coil_ids = master_df["Coil ID"].unique()

# Columns you want to map from each coil file
columns_to_map = [
    "STD4_ID",
    "rollingmode",
    "CM_WIDTH",
    "Grade",
]  # ← add/remove as needed

# Create dictionary of dictionaries
coil_info = {}

for coil_id in coil_ids:
    coil_file = os.path.join(coil_folder, f"{coil_id}.csv")
    if os.path.exists(coil_file):
        coil_df = pd.read_csv(coil_file)
        info = {}
        for col in columns_to_map:
            if col in coil_df.columns:
                info[col] = coil_df[col].iloc[0]
            else:
                info[col] = None
        coil_info[coil_id] = info

# Map all selected columns
for col in columns_to_map:
    master_df[col] = master_df["Coil ID"].map(lambda x: coil_info.get(x, {}).get(col))

# Save updated master file
master_df.to_csv("coil_anomaly_volatility_phasewise_good_merged.csv", index=False)

print("Merged successfully with additional columns:", columns_to_map)

