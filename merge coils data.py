# Import Libraries

import glob

import pandas as pd

csv_files = glob.glob(
    "D:/Stelco/Work/Dynamic Correlation/Key/Whole_Phase_Good_Clustered_Filtered/*.csv"
)  # Adjust as needed
output_csv = "combined_good_coil_data_filtered.csv"
write_header = True  # Write header only once


# Select Columns to Keep

selected_columns = [
    "Coil ID",
    "Coil Length [30ms]",
    "Master Ramp",
    "Stand 1 Predicted Run Force",
    "Stand 1 Gap Stick Offset",
    "Tension Reel Calculated Tension",
    "Tension To Gap 2 In Limit",
    "Stand 1-2 Total Tension Feedback",
    "Ramp Greater Than Thread",
    "Stand 3 - Operator Side Force",
    "Flatness Control - Bending In Limit",
    "Stand 1 Run Gap Setpoint",
    "Stand 1 Gap Bite Offset",
    "S1 Operating Bending Trim",
    "Stand 2-3 Tension Reference",
    "Neet Oil Concentration",
    "Morgoil DriveTop Bearing Outflow Temp Stand1",
    "Stand 4 Top Current Feedback",
    "Morgoil DriveTop Bearing Outflow Temp Stand3",
    "Stand 3 Run Gap Setpoint",
    "Stand 2 Total Bending Feedback",
    "Stand 2 Gap Bite Offset",
    "Morgoil OperBottom Bearing Outflow Temp Stand3",
    "Stand 4 Thread Gap Setpoint",
    "X4 Gauge Deviation",
    "Stand 4 DS Total Bending Feedback",
    "Laser 0 Data Valid",
    "Stand 4 - Operator Side Force",
    "Stand 2 Gap Eccentricity Trim",
    "Stand 4 Gap Operator Offset",
    "Stand 3 Total Bending Feedback",
    "Strip In Stand 3",
    "Morgoil OperTop Bearing Outflow Temp Stand1",
    "Strip In Stand 1",
    "X1 Gauge Deviation",
    "Stand 3 Drive Speed Feedback",
    "Stand 2 Gap Thread Offset",
    "Stand 2 Drive Speed Feedback",
    "Stand 1-3 Solution System Pressure",
    "Stand 2 Top Current Feedback",
    "Stand 1-3 Solution Temperature",
    "AGC GE Feedforward Hardness Number",
    "Stand 1 Total Bending Feedback",
    "X0 Gauge Deviation",
    "Stand 3 Bottom Current Feedback",
    "Stand 4 Gap Eccentricity Trim",
    "Stand 2 Gap Stick Offset",
    "Stand 3-4 Tension Reference",
    "Stand 4 Bottom Current Feedback",
    "Stand 1 Bottom Current Feedback",
    "Stand 3 Gap Thread Offset",
    "Stand 2 Bottom Current Feedback",
    "Stand 4 Solution System Pressure",
    "Stand 3 Gap Eccentricity Trim",
    "Stand 4 OS Total Bending Feedback",
    "Stand 1 Gap Thread Offset",
    "AGC Alex Dynamic Feedforward Hardness Number",
    "Stand 3 Top Current Feedback",
    "S2 Operating Bending Trim",
    "Roll Force Hydraulic Tank Level Inches",
    "Roll Force Hydraulics Pressure Feedback",
    "Stand 1 Roll Force Increase Limit (based on predicted run force)",
    "Stand 4 OS Bending Shape Trim",
    "Stand 4 DS Bending Shape Trim",
    "Phase",
    "STD4_ID",
]


# Merging

for csv_file in csv_files:
    df = pd.read_csv(csv_file, low_memory=False)
    if selected_columns is not None:
        df = df[selected_columns]
    df.to_csv(output_csv, mode="a", header=write_header, index=False)
    write_header = False  # Don't repeat header after first file

print("All files appended to:", output_csv)

