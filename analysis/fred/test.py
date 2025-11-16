import pandas as pd
import plotly.express as px
from IPython.core.display_functions import display

# Read the file
input_file = "../astha/immovlan_cleaned_file.csv"
df = pd.read_csv(input_file)
df["type"] = df["type"].str.lower().str.strip()

# Investment property
investment_property = df[df["type"] == "investment-property"]

# Garage
garage_types = ["garage", "parking"]    # Subcategories of "garage"
garage = df[df["type"].isin(garage_types)].reset_index(drop=True)   # If it's in garage_types, it is added to the list

# Undefined property
undefined_property = df[df["type"] == "undetermined-property"]

# Student housing
student_housing = df[df["type"] == "student-flat"]

# drop rows without coordinates
geo = investment_property.dropna(subset=["latitude", "longitude"])

fig = px.scatter_mapbox(geo,
                        lat="latitude", lon="longitude",
                        color="price_num",
                        size="price_num",
                        hover_data=["title", "price"],
                        color_continuous_scale=px.colors.cyclical.IceFire,
                        zoom=7,
                        title="Investment properties on the map")
fig.update_layout(mapbox_style="open-street-map")
fig.show()



