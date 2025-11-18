import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Read the file
input_file = "../astha/immovlan_cleaned_file.csv"
df = pd.read_csv(input_file)
df["type"] = df["type"].str.lower().str.strip()

# Investment property
investment_property = df[df["type"] == "investment-property"].copy()
#print(investment_property.describe())

# Garage
garage_types = ["garage", "parking"]    # Subcategories of "garage"
garage = df[df["type"].isin(garage_types)].reset_index(drop=True)   # If it's in garage_types, it is added to the list

# Undefined property
undefined_property = df[df["type"] == "undetermined-property"]

# Student housing
student_housing = df[df["type"] == "student-flat"]

# Correlation heat-map
def corr_heatmap(df, title, min_periods=5):
    """
    df : pd.DataFrame  – the slice to analyse
    title     : str           – plot title
    min_periods : int         – min observations to compute a correlation
    """

    # Keep only numeric columns
    num_df = df.select_dtypes(include=["number"])
    if num_df.shape[1] < 2:
        print(f"'{title}' has < 2 numeric columns - skipping correlation plot.")
        return

    # Compute correlations
    corr = num_df.corr(min_periods=min_periods)

    # Plot
    plt.figure(figsize=(8, 6))
    sns.heatmap(
        corr,
        annot=True,
        fmt=".2f",
        cmap="coolwarm",
        vmin=-1,
        vmax=1,
        square=True,
        linewidths=0.5,
    )

    plt.title(f"Correlation matrix - {title}")
    plt.tight_layout()
    plt.show()

# Draw the graph for every slice
for name, slice_df in {
    "Investment Property": investment_property,
    "Garage / Parking": garage,
    "Student Housing": student_housing,
    "Undetermined Property": undefined_property,
}.items():
    corr_heatmap(slice_df, name)

# Create a csv file for every property type
#for property_type in df["type"].unique():
#    df[df["type"] == property_type].to_csv(f"{property_type}.csv", index=False)