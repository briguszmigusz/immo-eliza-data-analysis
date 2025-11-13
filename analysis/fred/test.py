import pandas as pd
from IPython.core.display_functions import display

# Read the file
input_file = "../astha/immovlan_cleaned_file.csv"
df = pd.read_csv(input_file)
df["type"] = df["type"].str.lower().str.strip()

# Investment property
investment_property = df[df["type"] == "investment-property"].copy()
print(investment_property.describe())

# Garage
garage_types = ["garage", "parking"]    # Subcategories of "garage"
garage = df[df["type"].isin(garage_types)].reset_index(drop=True)   # If it's in garage_types, it is added to the list

# Undefined property
undefined_property = df[df["type"] == "undetermined-property"]

# Student housing
student_housing = df[df["type"] == "student-flat"]

# Create a csv file for every property type
#for property_type in df["type"].unique():
#    df[df["type"] == property_type].to_csv(f"{property_type}.csv", index=False)