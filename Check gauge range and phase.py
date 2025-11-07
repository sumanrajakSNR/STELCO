# Import Libraries
import pandas as pd

# Load Data
df = pd.read_csv(r"combined_good_coil_data_filtered_added gauge target and phases.csv")


# Apply necessary Filters
# df2 = df[(df['Phase'] == 'Phase 2') & df['X4 Gauge Deviation']<0.08]
df2 = df[df["X4 Gauge Deviation"] < 0.08]


# Save the modified csv
# df2.to_csv(r"C:\Users\USER\Desktop\Jupyter Notebook\Stelco\combined_good_coil_data_added gauge target and phases_Phase 2.csv",index=False)
df2.to_csv(
    r"combined_good_coil_data_filtered_added gauge target and phases_Gauge lst 0.08_std4.csv",
    index=False,
)



