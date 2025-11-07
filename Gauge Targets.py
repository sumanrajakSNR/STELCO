# Import Libraries
import os

import pandas as pd


# Calculate Gauge Target
def calculate_x4_target_only(csv1, csv2):
    # Load CSVs
    df1 = pd.read_csv(csv1)  # Static Data
    df2 = pd.read_csv(csv2)  # Time Series Data
    print(df2.shape)
    # Create mapping dict for CP_X4GAUGE
    cp_x4_map = df1.set_index("STD4_ID")["CP_X4GAUGE"].to_dict()

    # Function to get CP_X4GAUGE for coil id and multiply by X4 Gauge Deviation
    def calc_x4_target(row):
        cp_val = cp_x4_map.get(row["Coil ID"])
        if cp_val is None:
            return None  # or 0, or np.nan as preferred
        return row["X4 Gauge Deviation"] * cp_val

    # Apply function for entire df2
    df2["X4 Gauge Target"] = df2.apply(calc_x4_target, axis=1)

    return df2


# Example usage:
file1 = "D:/Stelco/Work/Dynamic Correlation/4stand_Metadata_static.csv"
file2 = "combined_good_coil_data_filtered.csv"
output_csv = "combined_good_coil_data_filtered_added gauge target and phases.csv"
# Clear the output file if it exists
if os.path.exists(output_csv):
    os.remove(output_csv)

result_df = calculate_x4_target_only(file1, file2)
result_df.to_csv(output_csv, index=False)




