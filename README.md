# Student Activities

A collection of weekly, hands-on learning projects completed as part of two student technical teams at **Mansoura University**: **IEEE (Mansoura Student Branch)** and **Mansoura Robotics**. Both tracks follow a similar arc — starting from core Python/data tools and progressing toward full data analysis, visualization, and machine learning workflows — but are organized as independent, self-contained tracks.

## Repository Structure

```
student_activities/
├── IEEE/                  # IEEE Mansoura Student Branch track
│   ├── week1-Numpy/
│   ├── week2-Pandas/
│   ├── week3-Library_Project/
│   ├── week4-Data_Cleaning/
│   ├── week5-Matplotlib/
│   ├── week6-Seaborn/
│   └── week7-Power_BI/
└── Mansoura_Robotics/     # Mansoura Robotics team track
    ├── week1-Assessment/
    ├── week2-Pillow/
    ├── week3-Pandas/
    ├── week4-EDA/
    ├── week5-Maplotlib_Seaborn_Encoding/
    ├── week6-Linear_Algebra/
    └── week7-Linear_Regression/
```

Each top-level folder has its own README with a full weekly breakdown.

---

## IEEE (Mansoura Student Branch)

**Folder:** [`IEEE/`](./IEEE)

IEEE Mansoura Student Branch is a student-run technical team at Mansoura University's Faculty of Engineering. This track builds core data analysis skills in Python, progressing from NumPy/Pandas fundamentals through data cleaning, visualization, and business intelligence.

| Week | Topic | Description |
|---|---|---|
| week1-Numpy | NumPy Fundamentals | Arrays, indexing, and vectorized operations |
| week2-Pandas | Pandas Fundamentals | Core DataFrame operations (selection, filtering, aggregation) on a students dataset |
| week3-Library_Project | Library Management Project | Small project working with books, members, and borrowings data |
| week4-Data_Cleaning | Data Cleaning | Cleans the 2017 Halloween Candy Hierarchy survey dataset — missing values, inconsistent text, tidy reshaping |
| week5-Matplotlib | Data Visualization | Visualizes an airline dataset with Matplotlib |
| week6-Seaborn | EDA with Seaborn | Exploratory analysis of a ~9,800-movie dataset (popularity, ratings, genre, language trends) |
| week7-Power_BI | Business Intelligence | A Power BI dashboard analyzing telecom customer churn (KPI cards, charts, DAX measures) |

**Requirements:** `numpy`, `pandas`, `matplotlib`, `seaborn`, `fuzzywuzzy`, `pycountry`, Power BI Desktop (for week 7)

---

## Mansoura Robotics

**Folder:** [`Mansoura_Robotics/`](./Mansoura_Robotics)

Mansoura Robotics is a student-run robotics and AI team at Mansoura University. This track moves from core Python fundamentals through image processing and data analysis, into visualization, linear algebra theory, and machine learning.

| Week | Topic | Description |
|---|---|---|
| week1-Assessment | Python Assessment | Core Python, NumPy, and Pandas practice projects |
| week2-Pillow | Image Processing | ASCII art image converter using NumPy + Pillow |
| week3-Pandas | Pandas | Automobile data analysis and price prediction |
| week4-EDA | Exploratory Data Analysis | Cleaning and analyzing a "dirty" cafe sales dataset |
| week5-Maplotlib_Seaborn_Encoding | Visualization & Encoding | Student performance factors analysis (encoding, scaling, correlation) |
| week6-Linear_Algebra | Linear Algebra | Handwritten notes on vectors, matrices, and linear systems |
| week7-Linear_Regression | Linear Regression | Titanic fare prediction model |

**Requirements:** `numpy`, `pandas`, `matplotlib`, `seaborn`, `scikit-learn`, `Pillow`

---

## About the Teams

- **IEEE Mansoura Student Branch** and **Mansoura Robotics** are both student-led technical teams based at the **Faculty of Engineering, Mansoura University**, Egypt.
- Both teams run structured, hands-on training programs for members — covering programming, data analysis, machine learning, and related engineering/robotics skills — through weekly assignments and projects like the ones in this repository.

## How to Use This Repo

1. Pick a track (`IEEE/` or `Mansoura_Robotics/`) and a week folder.
2. Open the week's notebook (`.ipynb`) in Jupyter, or the relevant script/file (`.py`, `.pdf`, `.pbix`).
3. Make sure any referenced data files (CSV/XLSX) are in the same folder, or update the file path in the notebook if needed.
4. Check that folder's own `README.md` for a detailed walkthrough of that week's steps and findings.

## Requirements (All Tracks Combined)

```
numpy
pandas
matplotlib
seaborn
scikit-learn
Pillow
fuzzywuzzy
pycountry
```

Install everything with:
```bash
pip install numpy pandas matplotlib seaborn scikit-learn Pillow fuzzywuzzy pycountry
```

Power BI Desktop is additionally required to open the `.pbix` file in `IEEE/week7-Power_BI`.
