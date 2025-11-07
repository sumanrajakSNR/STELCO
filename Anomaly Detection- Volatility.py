# Import Libraries
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Load Data
df = pd.read_csv(
    "combined_bad_coil_data_added gauge target and phases_Gauge lst 0.08_std4.csv"
)

# Specify only the IBA signal columns (edit this list)
iba_signals = [
    "Shape Target Second Coefficient",
    "Stand 1 Predicted Run Force",
    "Stand 1 Gap Stick Offset",
    "Tension Reel Calculated Tension",
    "Stand 1-2 Total Tension Feedback",
    "Stand 3 - Operator Side Force",
    "Stand 1 Run Gap Setpoint",
    "Stand 1 Gap Bite Offset",
    "S1 Operating Bending Trim",
    "Stand 2-3 Tension Reference",
    "Stand 3 Predicted Run Force",
    "Neet Oil Concentration",
    "Morgoil DriveTop Bearing Outflow Temp Stand1",
    "Stand 4 Top Current Feedback",
    "Morgoil DriveTop Bearing Outflow Temp Stand3",
    "Stand 2-3 Total Tension Feedback",
    "Stand 2 Predicted Run Force",
    "Stand 4 Gap Thread Offset",
    "Stand 2 - Operator Side Force",
    "Stand 3 Run Gap Setpoint",
    "Stand 2 Total Bending Feedback",
    "Stand 2 Gap Bite Offset",
    "Morgoil OperBottom Bearing Outflow Temp Stand3",
    "Exit Tension Reel Tension Reference",
    "Stand 4 Thread Gap Setpoint",
    "X4 Gauge Deviation",
    "Stand 4 DS Total Bending Feedback",
    "Stand 4 Gap Stick Offset",
    "Stand 4 - Operator Side Force",
    "Stand 2 Gap Eccentricity Trim",
    "Stand 4 Gap Operator Offset",
    "Stand 3 Total Bending Feedback",
    "Morgoil OperTop Bearing Outflow Temp Stand1",
    "Stand 1 - Operator Side Force",
    "X1 Gauge Deviation",
    "Stand 3 Drive Speed Feedback",
    "Stand 2 Gap Thread Offset",
    "Stand 4 Gap Bite Offset",
    "Stand 2 Drive Speed Feedback",
    "Stand 3 Thread Gap Setpoint",
    "Stand 1 Drive Speed Feedback",
    "Stand 1-3 Solution System Pressure",
    "Morgoil OperBottom Bearing Outflow Temp Stand4",
    "Stand 2 Thread Gap Setpoint",
    "Stand 2 Top Current Feedback",
    "Stand 1-3 Solution Temperature",
    "Stand 4 - Drive Side Force",
    "Stand 1 - Drive Side Force",
    "AGC GE Feedforward Hardness Number",
    "Stand 1 Total Bending Feedback",
    "Morgoil OperBottom Bearing Outflow Temp Stand1",
    "X0 Gauge Deviation",
    "Morgoil DriveTop Bearing Outflow Temp Stand4",
    "Stand 4 Predicted Run Force",
    "Stand 3 Bottom Current Feedback",
    "Stand 4 Gap Eccentricity Trim",
    "Morgoil DriveBottom Bearing Outflow Temp Stand1",
    "Stand 2 Gap Stick Offset",
    "Stand 3-4 Tension Reference",
    "Stand 4 Bottom Current Feedback",
    "Morgoil DriveTop Bearing Outflow Temp Stand2",
    "Stand 1 Bottom Current Feedback",
    "S3 Operating Bending Trim",
    "Morgoil DriveBottom Bearing Outflow Temp Stand4",
    "Stand 4 Drive Speed Feedback",
    "Stand 3 Gap Stick Offset",
    "Morgoil OperTop Bearing Outflow Temp Stand4",
    "Stand 3 Gap Thread Offset",
    "Morgoil OperBottom Bearing Outflow Temp Stand2",
    "Stand 3-4 Total Tension Feedback",
    "Morgoil OperTop Bearing Outflow Temp Stand2",
    "Stand 2 Gap Operator Offset",
    "Stand 2 Bottom Current Feedback",
    "Stand 2 - Total Force",
    "Stand 4 Solution System Pressure",
    "Stand 3 Gap Eccentricity Trim",
    "Stand 3 Gap Bite Offset",
    "Stand 2 - Drive Side Force",
    "Stand 4 OS Total Bending Feedback",
    "Morgoil DriveBottom Bearing Outflow Temp Stand2",
    "Stand 4 Run Gap Setpoint",
    "Stand 1-2 Tension Reference",
    "Stand 1 Gap Thread Offset",
    "Stand 1 Gap Operator Offset",
    "AGC Alex Dynamic Feedforward Hardness Number",
    "Stand 3 - Drive Side Force",
    "Stand 2 Run Gap Setpoint",
    "Stand 1 - Total Force",
    "Stand 1 Thread Gap Setpoint",
    "Stand 1 Top Current Feedback",
    "S4 Operating Bending Trim",
    "Stand 1 Gap Eccentricity Trim",
    "Master Ramp.1",
    "Stand 3 Top Current Feedback",
    "Morgoil DriveBottom Bearing Outflow Temp Stand3",
    "S2 Operating Bending Trim",
    "Morgoil OperTop Bearing Outflow Temp Stand3",
    "Stand 3 Gap Operator Offset",
    "Stand 1 Backup RPM",
    "Stand 2 Backup RPM",
    "Stand 3 Backup RPM",
    "Stand 4 Backup RPM",
    "Stand 1 Top Motor RPM",
    "Stand 1 Bottom Motor RPM",
    "Stand 2 Top Motor RPM",
    "Stand 2 Bottom Motor RPM",
    "Stand 3 Top Motor RPM",
    "Stand 3 Bottom Motor RPM",
    "Stand 4 Top Motor RPM",
    "Stand 4 Bottom Motor RPM",
    "Payoff Reel OS RPM",
    "Payoff Reel DS RPM",
    "Exit Tension Reel RPM",
    "Roll Force Hydraulic Tank Level Inches",
    "Stand 1 OS Roll Force",
    "Stand 2 OS Roll Force",
    "Stand 3 OS Roll Force",
    "Stand 4 OS Roll Force",
    "Stand 1 DS Roll Force",
    "Stand 2 DS Roll Force",
    "Stand 3 DS Roll Force",
    "Stand 4 DS Roll Force",
    "Roll Force Hydraulics Pressure Feedback",
    "Stand 1 Roll Force",
    "Stand 1 Roll Force limit (g67 delayed 200 ms + g80)",
    "Stand 1 Roll Force Increase Limit (based on predicted run force)",
    "Stand 4 OS Bending Shape Trim",
    "Stand 4 DS Bending Shape Trim",
    "Shape Target Second Coefficient.1",
]

# ---------------------------------------------------------------------------------------------
# All Phase Anomaly%

# def volatility_anomaly_detection(series, window=50, threshold_factor=2):
#     series = series.dropna().reset_index(drop=True)

#     # Rolling volatility
#     rolling_vol = series.rolling(window).std()

#     # Threshold
#     mean_vol = rolling_vol.mean()
#     std_vol = rolling_vol.std()
#     upper_threshold = mean_vol + threshold_factor * std_vol
#     lower_threshold = mean_vol - threshold_factor * std_vol

#     # Anomalies = volatility spikes
#     anomalies = rolling_vol[(rolling_vol > upper_threshold) | (rolling_vol < lower_threshold)]

#     anomaly_percentage = 100 * len(anomalies.dropna()) / len(series)
#     return anomaly_percentage

# results = []

# for coil_id, coil_group in df.groupby("Coil ID"):
#     coil_result = {"Coil ID": coil_id}
#     for signal in iba_signals:
#         if signal in coil_group.columns:
#             perc = volatility_anomaly_detection(coil_group[signal])
#             coil_result[signal] = perc
#         else:
#             coil_result[signal] = np.nan
#     results.append(coil_result)

# results_df = pd.DataFrame(results)
# results_df

# ---------------------------------------------------------------------------
# Phasewise Anomaly%

def volatility_anomaly_detection(series, window=50, threshold_factor=2):
    series = series.dropna().reset_index(drop=True)

    rolling_vol = series.rolling(window).std()

    mean_vol = rolling_vol.mean()
    std_vol = rolling_vol.std()
    upper_threshold = mean_vol + threshold_factor * std_vol
    lower_threshold = mean_vol - threshold_factor * std_vol

    anomalies = rolling_vol[
        (rolling_vol > upper_threshold) | (rolling_vol < lower_threshold)
    ]
    anomaly_percentage = (
        100 * len(anomalies.dropna()) / len(series) if len(series) > 0 else 0
    )

    return anomaly_percentage


results = []

for (coil_id, phase, std4_id), coil_phase_group in df.groupby(
    ["Coil ID", "Phase", "STD4_ID"]
):
    coil_phase_result = {"Coil ID": coil_id, "Phase": phase, "STD4_ID": std4_id}

    for signal in iba_signals:
        if signal in coil_phase_group.columns:
            perc = volatility_anomaly_detection(coil_phase_group[signal])
            coil_phase_result[f"{signal}"] = perc
        else:
            coil_phase_result[f"{signal}"] = np.nan

    results.append(coil_phase_result)

results_df = pd.DataFrame(results)
results_df["STD4_ID"] = results_df["STD4_ID"].astype(int)

# print(results_df)

# Save to CSV
results_df.to_csv("coil_anomaly_volatility_phasewise_bad_merged.csv", index=False)
print("Results saved.")




