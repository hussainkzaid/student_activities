# Automobile Data Analysis & Price Prediction (Pandas)

**File:** `pandas.ipynb`

A data analysis project built around the `Automobile_data.csv` dataset. It covers the full workflow from data cleaning and exploratory analysis with Pandas, through visualization, to a simple linear regression model that predicts car prices.

---

## Dataset
`Automobile_data.csv` — expected at `/content/Automobile_data.csv` (Google Colab path; update if running locally). Contains details on cars including company, engine type, number of cylinders, average mileage, horsepower, length, wheel base, and price.

---

## Workflow

### 1. Load & explore
- Imports the CSV into a DataFrame
- Inspects the data with `.head()` and `.info()` to review columns and datatypes

### 2. Data cleaning
- Identifies rows with missing values (`NaN`) in the `price` column — 3 rows found
- One row was a duplicate Isuzu entry → dropped
- The remaining Isuzu row's missing price was filled with the **mean price of similar cars** (same company or matching engine-type/cylinders/mileage)
- A missing Porsche price was filled with the **mean price of similar high-performance cars** (same company or horsepower > 250)
- Confirmed no columns required a datatype conversion

### 3. Exploratory analysis
Answers a series of guided questions using `groupby`, aggregation, and sorting:
- Most expensive car company (by total price)
- Full statistical summary of all Toyota cars (`.describe()`)
- Total car count per company
- Each company's highest-priced car
- Average mileage per company
- All cars sorted by price (descending)

### 4. Combining DataFrames
- **Concatenation**: Builds separate German and Japanese car-price DataFrames and stacks them with `pd.concat()`
- **Merging**: Builds separate price and horsepower DataFrames (keyed by company) and joins them with `.merge()` to add horsepower as a new column

### 5. Visualization
- Horizontal bar chart of car counts by engine type (Matplotlib)
- Correlation heatmap of all numeric features (Seaborn, masked to show only the lower triangle)

### 6. Price prediction model
- Selects `horsepower`, `average-mileage`, `length`, and `wheel-base` as features to predict `price`
- Splits data into train/test sets (80/20)
- Fits a **Linear Regression** model (scikit-learn) and prints the intercept and feature coefficients
- Evaluates performance on the test set with **R²** and **RMSE**
- Visualizes actual vs. predicted price distributions (KDE plot) and as a scatter plot against a "perfect prediction" reference line
- Demonstrates the model on:
  - A custom hypothetical car's specs
  - A real car from the dataset, comparing predicted vs. actual price and reporting the error

---

## Concepts practiced
- Data cleaning: detecting and imputing missing values based on similar-record logic
- Exploratory data analysis with `groupby`, aggregation functions (`sum`, `mean`, `max`, `count`), filtering, and sorting
- Combining datasets with `pd.concat()` and `pd.merge()`
- Data visualization with Matplotlib and Seaborn (bar charts, heatmaps, KDE plots, scatter plots)
- Correlation analysis between numeric features
- Building, training, and evaluating a linear regression model with scikit-learn
- Model evaluation metrics: R² score and RMSE
- Making and validating predictions on new/unseen data

---

## Requirements
- Python 3.x
- `pandas`
- `matplotlib`
- `seaborn`
- `numpy`
- `scikit-learn`

Install dependencies:
```bash
pip install pandas matplotlib seaborn numpy scikit-learn
```

## How to run
1. Place `Automobile_data.csv` in the directory the notebook expects (originally `/content/Automobile_data.csv` for Google Colab — update the path if running locally, e.g. Jupyter Notebook/Lab).
2. Run all cells in `pandas.ipynb` sequentially.
3. Review the printed outputs, charts, and final price prediction results.

## Results summary
- The cleaning step resolved all missing prices using domain-informed imputation (mean price of comparable cars) rather than simple mean/median fill.
- The linear regression model's performance (R² and RMSE) is printed in the notebook; predictions are validated against a real car's actual price to sanity-check the model.
