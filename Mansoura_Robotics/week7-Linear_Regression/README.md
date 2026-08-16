# Titanic Fare Prediction — Linear Regression

A notebook (`Linear_Regression.ipynb`) that loads and cleans the Titanic passenger dataset, explores it visually, and builds a linear regression model to predict passenger `Fare` from other passenger attributes.

## Dataset

- **Source file:** `titanic_large.csv`
- **Target variable:** `Fare`
- **Key columns:** `Survived`, `Pclass`, `Sex`, `Age`, `SibSp`, `Parch`, `Fare`, `Embarked`

## Workflow

### 1. Setup
Imports `pandas`, `numpy`, `matplotlib`, `seaborn`, and scikit-learn preprocessing tools (`MinMaxScaler`). Seaborn is set to the `darkgrid` style.

### 2. Load & Inspect
- Loads `titanic_large.csv` and previews it with `.head()`
- Summarizes column types and stats with `.info()` / `.describe()`
- Checks for missing values with `.isnull().sum()`

### 3. Clean
- Dropped rows with missing `Age`
- Converted `Age` from float to integer
- Re-checked for missing values in `Age` to confirm the fix

### 4. Exploratory Visualizations
- Gender distribution (histogram of `Sex`)
- Age distribution (histogram, 10 bins)
- Embarked port distribution (histogram)
- Passenger class breakdown (pie chart of `Pclass`)
- Survival by passenger class (count plot, split by `Survived`)
- Age distribution: all passengers vs. survivors (overlaid histograms)

### 5. Correlation Analysis
Computed and visualized (via heatmap) the correlation matrix for numeric features: `Survived`, `Pclass`, `Age`, `SibSp`, `Parch`, `Fare`.

### 6. Feature Engineering
Built a modeling copy of the data (`data_model`):
- `Sex` mapped to numbers: `male → 0`, `female → 1`
- `Embarked` mapped to numbers: `S → 0`, `C → 1`, `Q → 2`
- Relevant features (`Survived`, `Sex`, `Age`, `SibSp`, `Parch`, `Pclass`, `Embarked`) scaled to 0–1 with `MinMaxScaler`

### 7. Model
- **Inputs (X):** `Age`, `Sex`, `Pclass`, `SibSp`, `Parch`, `Survived`, `Embarked` (scaled)
- **Target (y):** `Fare` (unscaled)
- 80/20 train/test split (`random_state=42`)
- `sklearn.linear_model.LinearRegression` trained on the training set

### 8. Evaluation
Predictions on the test set are evaluated with:
- **R²** — variance in `Fare` explained by the model
- **MAE** — mean absolute error
- **RMSE** — root mean squared error

A KDE (density) plot compares the distribution of actual vs. predicted `Fare` values (x-axis limited to 0–100 for readability).

## Requirements

```
pandas
numpy
matplotlib
seaborn
scikit-learn
```

## Usage

1. Place `titanic_large.csv` in the same directory as the notebook (or update the file path in the load cell).
2. Run the notebook cells in order from top to bottom.
