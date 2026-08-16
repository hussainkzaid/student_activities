# Cafe Sales — Exploratory Data Analysis

An EDA notebook (`EDA.ipynb`) that loads, cleans, and analyzes a "dirty" cafe sales dataset, following a Load → Inspect → Clean → Detect Outliers → Analyze → Document workflow.

## Dataset

- **Source file:** `dirty_cafe_sales.csv`
- **Size:** 10,000 rows × 8 columns
- **Columns:** `Transaction ID`, `Item`, `Quantity`, `Price Per Unit`, `Total Spent`, `Payment Method`, `Location`, `Transaction Date`

## Workflow

### 1. Load
Imports pandas, numpy, matplotlib, and seaborn, then loads the CSV into a DataFrame.

### 2. Inspect
Checks shape, dtypes, and summary statistics with `.info()` and `.describe()`.

### 3. Clean
- Removed duplicate rows based on `Transaction ID`
- Replaced placeholder strings (`UNKNOWN`, `ERROR`) with `NaN` across all columns
- Converted numeric-looking columns (`Quantity`, `Price Per Unit`, `Total Spent`) from `object` to `float`
- Recovered missing values using the relationship `Total Spent = Quantity × Price Per Unit`
- Recovered missing `Item` / `Price Per Unit` values using a known item-to-price mapping
- Manually fixed a handful of rows with many missing values where the correct values could be inferred
- Dropped rows with too many missing values that couldn't be recovered

### 4. Outlier Detection
Reviewed summary statistics — no outliers found in the cleaned data.

### 5. Analysis
- Computed correlations between `Quantity`, `Price Per Unit`, and `Total Spent`
- Visualized correlations with a heatmap
- Plotted `Price Per Unit` vs. `Total Spent` (point size scaled by `Quantity`)

### 6. Findings

**Cleaning results:**
- 9,977 of 10,000 rows retained (98.8% of original data)
- `Item`, `Total Spent`, `Quantity`, and `Price Per Unit` have zero missing values after cleaning

**Correlation insights:**
- `Total Spent` correlates strongly with `Quantity` (r ≈ 0.70) and `Price Per Unit` (r ≈ 0.65)
- `Quantity` and `Price Per Unit` show essentially no correlation with each other (r ≈ 0.008)

## Requirements

```
pandas
numpy
matplotlib
seaborn
```

## Usage

1. Place `dirty_cafe_sales.csv` in the expected path (the notebook reads from `/content/dirty_cafe_sales.csv`, a Google Colab path — update this if running locally).
2. Run the notebook cells in order from top to bottom.
