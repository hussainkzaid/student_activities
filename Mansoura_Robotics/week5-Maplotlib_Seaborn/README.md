# Student Performance — Exploratory Data Analysis

An EDA notebook (`Student_performance.ipynb`) that loads, cleans, encodes, and analyzes a student performance dataset, exploring which factors relate to students' previous exam scores.

## Dataset

- **Source file:** `StudentPerformanceFactors-selected-columns.csv`
- **Size:** 6,607 rows × 10 columns
- **Quality:** no duplicates, no missing values
- **Columns:** `Hours_Studied`, `Attendance`, `Parental_Involvement`, `Access_to_Resources`, `Extracurricular_Activities`, `Sleep_Hours`, `Previous_Scores`, `Motivation_Level`, `Internet_Access`, `Tutoring_Sessions`

## Workflow

### 1. Load & Inspect
Imports pandas, matplotlib, and seaborn; loads the CSV; checks shape, dtypes, and summary statistics with `.info()` / `.describe()`.

### 2. Clean
- Dropped duplicate rows (none found)
- Checked for missing values (none found)
- Kept a copy of the original data (`data_vis`) for visualization before encoding/scaling

### 3. Encode Categorical Features
- **Ordinal encoding** (Low=0, Medium=1, High=2): `Parental_Involvement`, `Access_to_Resources`, `Motivation_Level`
- **Label encoding** (binary, via `sklearn.LabelEncoder`): `Extracurricular_Activities`, `Internet_Access`

### 4. Scale Numeric Features
Applied **Min-Max scaling** (0–1 range, via `sklearn.MinMaxScaler`) to `Hours_Studied`, `Attendance`, `Sleep_Hours`, `Previous_Scores`, `Tutoring_Sessions`.

### 5. Analysis & Visualization
Explored relationships between various factors and `Previous_Scores` using bar plots, scatter plots, line plots, a pie chart, and a correlation heatmap:
- Average score by parental involvement level
- Average score by access to resources
- Average score by motivation level
- Attendance vs. previous scores
- Hours studied vs. previous scores
- Average score by sleep hours
- Average score by study hours
- Average score by internet access
- Correlation heatmap across scaled numeric features

### 6. Key Findings

- **Parental involvement, access to resources, and motivation level** each show a clear positive step-up in average `Previous_Scores` from Low → Medium → High — the strongest and most consistent signals in the data.
- **Attendance vs. Previous_Scores:** essentially no linear correlation (r ≈ -0.02).
- **Hours_Studied vs. Previous_Scores:** essentially no linear correlation (r ≈ 0.02); scores stay roughly flat (~74–78) across the study-hours range.
- **Sleep_Hours vs. Previous_Scores:** nearly flat average (~74–76) across 4–10 hours of sleep — no meaningful relationship.
- **Internet_Access vs. Previous_Scores:** nearly identical average scores for Yes (75.1) and No (74.9) despite class imbalance — negligible effect.
- **Correlation heatmap:** all off-diagonal correlations among the scaled numeric features are close to 0, confirming these continuous features are largely independent of each other and of `Previous_Scores`.

## Requirements

```
pandas
matplotlib
seaborn
scikit-learn
```

## Usage

1. Place `StudentPerformanceFactors-selected-columns.csv` in the same directory as the notebook (or update the file path in the load cell).
2. Run the notebook cells in order from top to bottom.
