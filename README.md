# 🐯 Team Tiger – Immo Eliza Real Estate Analysis

## 📌 Project Overview

This repository contains the full data cleaning and exploratory data analysis for the **Immo Eliza** dataset.  
The objective of this project is to uncover insights about the Belgian real-estate market and determine which variables have the strongest impact on property prices.  
All results are prepared for a non-technical audience.

Our work focuses on:

- Consistent data cleaning  
- Feature engineering (postcode, city, province, type)  
- Exploratory data analysis  
- Visualisation using Plotly & Seaborn  
- Regional and provincial price comparisons  
- Property type segmentation  
- Correlation analysis  
- A clear, presentation-ready summary for stakeholders  

---

## 🗂 Repository Structure
```
immo-eliza-data-analysis/
│
├── analysis/
│   ├── astha/
│   │   ├── data_cleaning.ipynb
│   │   ├── immovlan_cleaned_file.csv
│   │   └── final_visual_analysis.ipynb      <-- MAIN analysis notebook used for the presentation
│   │
│   ├── brigi/
│   │   ├── brigi_data_cleaning.ipynb
│   │   ├── cleaned_data.csv
│   │   └── immovlan_final_file.csv
│   │
│   ├── esra/
│   │   ├── dev_esra_notebook.ipynb
│   │   ├── esrafile_v1.csv
│   │   ├── Immovlan_EDA_and_cleaning.ipynb
│   │   └── immovlan_final_file.csv
│   │
│   └── pierrick/
│       ├── pierrick_analysis.ipynb
│       ├── correlationHeatmap.png
│       └── final_analysis.ipynb
│  
│
├── data/
│   ├── raw/
│   │   ├── immo_eliza_raw.csv
│   │   └── immovlan_final_file.csv
│   │
│   ├── cleaned/
│   │   ├── immo_eliza_cleaned.parquet
│   │   └── cleaned-dataset/
│   │       └── (final processed files)
│
├── reports/
│   ├── finalized-presentation.pdf
│   └── figures/                 <-- Exported graphs & charts
│
├── utils/
│   └── .gitignore       
│
├── requirements.txt
└── README.md                    
```

---

## 🧼 Data Cleaning – Team Roles

### **Pierrick – Data Cleaning & Preparation for Analysis**
- Built the complete cleaning pipeline  
- Normalised all column names and text formats  
- Engineered key features with the code from the others: `postcode`, `city`, `province`, `property_category`, `price_per_m2`  
- Ensured consistent numeric types (aigain with help of others), removed outliers, fixed encoding issues  
- Structured the dataset so every team member could work on analysis smoothly  

### **Brigi – Repository Manager & URL Feature Extraction**
- Extracted postcode and city from URLs  
- Helped structure the dataset with new meaningful features  
- Produced several visualisations  
- Maintained branch discipline and resolved repository conflicts  
- Ensured our GitHub structure stayed clean and conflict-free  

### **Astha – Team Lead**
- Distributed tasks and set clear project goals  
- Coordinated daily progress check-ins  
- Ensured alignment in analysis direction  
- Participated in reviewing cleaning steps and visualisation ideas  

### **Esra – Visualisation & Planning**
- Created visualisation prototypes and experimented with multiple graph types  
- Helped structure the flow of analysis topics  
- Worked on planning and kept track of deadlines during the week  

### **Fred – Province Mapping & Type Segmentation**
- Implemented Belgian postcode → province logic  
- Supported the breakdown of data by property type  
- Helped validate intermediate cleaning decisions and cross-checked dataset consistency  

---

## 📊 Analysis Contents

Our analysis answers the key questions required by the project:

- How many rows and columns does the dataset contain?  
- What is the percentage of missing values?  
- Which columns require cleaning or removal?  
- How are **prices** and **price per m²** distributed?  
- What are the **most expensive regions and provinces**?  
- How does property type influence price?  
- Which variables correlate most strongly with price?  
- What can we conclude about the Belgian housing market today?  

All results are illustrated using clear, accessible visualisations.

---

## 🔍 Key Insights

### **1. Regional Differences**
- Brussels is the most expensive region by a large margin.  
- Flanders ranks second, followed by Wallonia.  

### **2. Provincial Differences**
- The highest prices appear in  
  **Brussels, Antwerp, and Flemish Brabant**.  
- Walloon provinces show lower prices, except parts of Liège.

### **3. Property Type**
- Apartments have a higher €/m² than houses  
- Houses show higher sensitivity to land size and number of bathrooms

### **4. Correlation Findings**
- Strongest predictors of price:  
  **bathrooms, toilets, bedrooms**  
- Livable surface is a weak predictor  
- Functionality > size  
- Correlations vary across property types  

---

## 🐯 Team Tiger Summary

This project is the result of strong teamwork. Each member contributed to critical parts of the pipeline, from cleaning to feature extraction to analysis and visualisation. Together, we transformed raw scraped listings into actionable real-estate insights for Immo Eliza.



