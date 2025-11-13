# 🏡 Belgium Housing Price Prediction – EDA & Data Cleaning Plan

**Goal:**  
Build a data-driven model to predict house prices in Belgium using Immovlan data (16,309 rows × 26 columns).  
This week’s focus: **Data Cleaning + Exploratory Data Analysis (EDA)** before modeling.  

---

## 📊 1. Dataset Summary

**File:** `immovlan_final_file.csv`  
**Rows:** 16,309  
**Columns:** 26  

| Feature | Notes |
|----------|--------|
| `Price` | Target variable – needs numeric conversion |
| `Livable surface`, `Surface garden`, `Surface terrace` | Contain units (m²) → clean & convert to float |
| `Garage`, `Swimming pool`, `Kitchen type`, `Attic` | High missing rate → categorical |
| `Number of bedrooms`, `bathrooms`, `toilets` | Numeric, may contain NaN |
| `Property ID`, `url` | Identifiers, not needed for modeling |

---

## 🧹 2. Data Cleaning – Key Steps

### 💰 Price Cleaning
```python
df['Price'] = (
    df['Price']
    .astype(str)
    .str.replace("€", "", regex=False)
    .str.replace(",", "", regex=False)
    .str.replace(".", "", regex=False)
    .str.strip()
)
df['Price'] = pd.to_numeric(df['Price'], errors='coerce')
```

### 📏 Surface Columns Cleaning
```python
surface_cols = ['Livable surface', 'Surface garden', 'Surface terrace', 'Total land surface']
for col in surface_cols:
    df[col] = (
        df[col]
        .astype(str)
        .str.replace("m²", "", regex=False)
        .str.replace(",", "", regex=False)
        .str.strip()
    )
    df[col] = pd.to_numeric(df[col], errors='coerce')
```

### 🔍 Missing Value Overview
```python
df.isnull().sum().sort_values(ascending=False).head(15)
```

---

## 📈 3. Exploratory Data Analysis (EDA)

### Step 1: General Overview
```python
print("Dataset shape:", df.shape)
df.info()
df.describe().T
```

---

## 💡 4. 15 Key Analytical Questions (Team-Based)

Each team member can take 3 questions and share insights in Trello.

### 🏠 A. General Overview
1. What is the **mean, median, and standard deviation** of prices?  
   ```python
   df['Price'].describe()
   ```
2. Which **5 regions/postcodes** have the highest and lowest average prices?  
   ```python
   df.groupby('postcode')['Price'].mean().sort_values(ascending=False).head(5)
   ```
3. Is the price distribution **log-normal**? Plot histograms before & after log transform.  
   ```python
   import matplotlib.pyplot as plt
   import numpy as np

   plt.hist(df['Price'].dropna(), bins=50)
   plt.title('Price Distribution')
   plt.show()

   plt.hist(np.log1p(df['Price'].dropna()), bins=50)
   plt.title('Log Price Distribution')
   plt.show()
   ```

---

### 📏 B. Physical Characteristics
4. How does **Livable surface** correlate with price?  
   ```python
   df[['Livable surface', 'Price']].corr()
   plt.scatter(df['Livable surface'], df['Price'])
   ```
5. How does the **number of bedrooms** affect the average price?  
   ```python
   df.groupby('Number of bedrooms')['Price'].mean()
   ```
6. Is there a visible relationship between **number of bathrooms** and price?  
   ```python
   df.groupby('Number of bathrooms')['Price'].mean().plot(kind='bar')
   ```

---

### 🌳 C. Amenities
7. Do houses **with a garden** cost more than those without?  
   ```python
   df.groupby('Garden')['Price'].mean()
   ```
8. Does having a **garage** increase average price?  
   ```python
   df.groupby('Garage')['Price'].mean()
   ```
9. Is there a **price premium** for homes with a **swimming pool**?  
   ```python
   df.groupby('Swimming pool')['Price'].mean()
   ```
10. Does **terrace size** correlate with price?  
    ```python
    df[['Surface terrace', 'Price']].corr()
    ```

---

### 🌍 D. Location & Socioeconomic Factors
11. How do prices vary by **postcode** or **city**?  
    ```python
    df.groupby('postcode')['Price'].mean().sort_values(ascending=False).head(10)
    ```
12. Are **expat-dominant areas** (e.g., Tervuren, Waterloo, Uccle) more expensive than others?  
    ```python
    expat_zips = [3080, 1410, 1180]
    df[df['postcode'].isin(expat_zips)]['Price'].mean()
    ```
13. Does **distance from city center or university** impact price? (use proxies or postal zones)

---

### 🔥 E. Property Condition
14. How does **“State of the property”** (new, renovated, to renovate) affect price?  
    ```python
    df.groupby('State of the property')['Price'].mean()
    ```
15. Are **recently built** homes consistently more expensive?  
    _(if construction year available, otherwise use “State of the property”)_

---

## 🧩 5. Team Workflow Plan (3-Hour Session)

| Time | Phase | Objective |
|------|--------|------------|
| 0:00–0:30 | Data Cleaning | Fix `Price`, `Surface` columns, handle missing data |
| 0:30–1:30 | EDA & Visualizations | Histograms, scatter plots, correlations |
| 1:30–2:30 | Team Questions | Each member answers 3 assigned questions |
| 2:30–3:00 | Wrap-up | Discuss findings – key factors driving house prices |

---

## 📘 6. Deliverables

- ✅ Clean dataset (`immovlan_clean.csv`)  
- 📊 EDA notebook (`immovlan_eda.ipynb`)  
- 🧩 Team insights summary (15 questions answered)  
- 💬 Discussion in Trello or shared document  
