# Mansoura Robotics — Student Activities

A weekly progression of hands-on Python and data-science exercises, moving from core Python fundamentals through image processing, data analysis, visualization, and into machine learning and its mathematical foundations.

## Weeks Overview

| Week | Topic | Contents |
|------|-------|----------|
| [Week 1](./week1-Assessment) | Python Assessment | Core Python, NumPy, and Pandas practice projects |
| [Week 2](./week2-Pillow) | Pillow (Image Processing) | ASCII Art Image Converter |
| [Week 3](./week3-Pandas) | Pandas | Automobile Data Analysis & Price Prediction |
| [Week 4](./week4-EDA) | Exploratory Data Analysis | Cafe Sales EDA |
| [Week 5](./week5-Maplotlib_Seaborn_Encoding) | Matplotlib, Seaborn & Encoding | Student Performance Factors analysis |
| [Week 6](./week6-Linear_Algebra) | Linear Algebra | Handwritten notes on vectors, matrices, and linear systems |
| [Week 7](./week7-Linear_Regression) | Linear Regression | Titanic Fare Prediction |

---

## Week 1 — Python Assessment
**Folder:** `week1-Assessment`

Three small Python projects covering plain Python data structures, NumPy array operations, and Pandas-based data management with a CLI interface:

- **Student Score System** (`Student_Score_System.py`) — console program that collects student names/grades and reports pass/fail status using dictionaries, loops, and sets.
- **Small Electronics Store** (`small_electronics_store..py`) — NumPy-based sales analysis (monthly/total revenue, top performers, filtering, broadcasting).
- **Student Management System** (`Student_Management_System.py`) — interactive, menu-driven CLI with full CRUD operations on a Pandas DataFrame (add/search/update/delete/show students).

**Requirements:** `numpy`, `pandas`

---

## Week 2 — Pillow (Image Processing)
**Folder:** `week2-Pillow`

**ASCII Art Image Converter** (`ASCII Art Image Converter.ipynb`) — converts an image into ASCII art using NumPy for pixel manipulation and Pillow for image I/O. Produces both grayscale and colored ASCII art:

1. Loads image → NumPy array
2. Converts to grayscale via the luminosity formula
3. Downsamples into blocks (image pooling)
4. Maps brightness to ASCII characters (`@%#*+=-:.`) via `np.interp`
5. Renders grayscale ASCII art (`photo_text.png`)
6. Renders colored ASCII art using each block's average RGB color (`photo_colored.png`)

**Requirements:** `numpy`, `Pillow`

---

## Week 3 — Pandas
**Folder:** `week3-Pandas`

**Automobile Data Analysis & Price Prediction** (`Automobile Data Analysis & Price Prediction.ipynb`) — full workflow on `Automobile_data.csv`, from cleaning through visualization to a simple linear regression price model:

1. **Load & explore** — inspect columns/dtypes
2. **Clean** — handle missing `price` values (drop duplicate, impute using means of similar cars)
3. **Exploratory analysis** — most expensive company, per-company stats, average mileage, price rankings via `groupby`
4. **Combine DataFrames** — concatenation (German vs. Japanese cars) and merging (price + horsepower by company)
5. **Visualization** — bar chart of engine types, correlation heatmap
6. **Modeling** — linear regression to predict car price

**Requirements:** `pandas`, `numpy`, `matplotlib`, `seaborn`, `scikit-learn`

---

## Week 4 — Exploratory Data Analysis
**Folder:** `week4-EDA`

**Cafe Sales EDA** (`Cafe Sales — Exploratory Data Analysis.ipynb`) — cleans and analyzes a "dirty" cafe sales dataset (`dirty_cafe_sales.csv`, 10,000 rows):

1. **Load & inspect** — shape, dtypes, summary stats
2. **Clean** — remove duplicates, replace placeholder strings (`UNKNOWN`/`ERROR`) with `NaN`, convert numeric columns, recover missing values via `Total Spent = Quantity × Price Per Unit` and known item-price mappings, drop unrecoverable rows
3. **Outlier detection** — none found after cleaning
4. **Analysis** — correlation heatmap and scatter plot of `Price Per Unit` vs. `Total Spent`

**Key findings:** 9,977 of 10,000 rows retained (98.8%); `Total Spent` correlates strongly with `Quantity` (r ≈ 0.70) and `Price Per Unit` (r ≈ 0.65); `Quantity` and `Price Per Unit` are essentially uncorrelated (r ≈ 0.008).

**Requirements:** `pandas`, `numpy`, `matplotlib`, `seaborn`

---

## Week 5 — Matplotlib, Seaborn & Encoding
**Folder:** `week5-Maplotlib_Seaborn_Encoding`

**Student Performance Factors** (`Student_performance.ipynb`) — explores which factors relate to students' previous exam scores (`StudentPerformanceFactors-selected-columns.csv`, 6,607 rows):

1. **Load & inspect** — no duplicates, no missing values
2. **Encode** — ordinal encoding (Low/Medium/High → 0/1/2) for `Parental_Involvement`, `Access_to_Resources`, `Motivation_Level`; label encoding for `Extracurricular_Activities`, `Internet_Access`
3. **Scale** — Min-Max scaling of numeric features
4. **Visualize & analyze** — bar/scatter/line plots and a correlation heatmap

**Key findings:** parental involvement, access to resources, and motivation level each show a clear positive step-up in average scores (Low → Medium → High). Attendance, hours studied, sleep, and internet access show negligible correlation with previous scores.

**Requirements:** `pandas`, `matplotlib`, `seaborn`, `scikit-learn`

---

## Week 6 — Linear Algebra
**Folder:** `week6-Linear_Algebra`

Handwritten notes (`Linear_Algebra.pdf`) covering foundational linear algebra:

- Vectors, vector spaces (R, R², R³, ... Rⁿ), and the L2 norm
- Law of Sines/Cosines, Euclidean distance
- Scalars vs. vectors, vector indexing, special vectors (zero, unit, sparse)
- Vector addition/subtraction, scalar multiplication, dot & inner products, Cauchy-Schwarz inequality
- Linear systems (homogeneous/nonhomogeneous), matrix definition and operations
- Solving linear systems: Gaussian elimination, Row Echelon Form, Reduced Row Echelon Form (with a fully worked 3×3 example), and the three possible solution cases (none, infinite, unique)

---

## Week 7 — Linear Regression
**Folder:** `week7-Linear_Regression`

**Titanic Fare Prediction** (`Linear_Regression.ipynb`) — loads and cleans the Titanic dataset (`titanic_large.csv`), explores it visually, and builds a linear regression model to predict passenger `Fare`:

1. **Load & inspect** — check missing values
2. **Clean** — drop rows with missing `Age`, convert `Age` to integer
3. **Exploratory visualizations** — gender/age/embarked distributions, class breakdown, survival by class, age vs. survival
4. **Correlation analysis** — heatmap of numeric features
5. **Feature engineering** — map `Sex` and `Embarked` to numbers, Min-Max scale features
6. **Model** — `LinearRegression` predicting `Fare` from `Age`, `Sex`, `Pclass`, `SibSp`, `Parch`, `Survived`, `Embarked` (80/20 train/test split)
7. **Evaluation** — R², MAE, RMSE, and a KDE plot comparing actual vs. predicted fares

**Requirements:** `pandas`, `numpy`, `matplotlib`, `seaborn`, `scikit-learn`

---

## General Requirements

Across all weeks, the following Python libraries are used:

```
numpy
pandas
matplotlib
seaborn
scikit-learn
Pillow
```

Install everything at once:
```bash
pip install numpy pandas matplotlib seaborn scikit-learn Pillow
```
