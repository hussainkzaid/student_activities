# IEEE Data Analysis Track — Weekly Projects

This repository collects a series of weekly, hands-on exercises building core data analysis skills in Python — from NumPy and Pandas fundamentals through data cleaning, visualization, and exploratory data analysis (EDA).

## Repository Structure

```
IEEE/
├── week1-Numpy/
│   ├── Numpy.ipynb
│   └── README.md
├── week2-Pandas/
│   ├── Pandas.ipynb
│   ├── Pandas_README.md
│   └── students_DataFrame.csv
├── week3-Library_Project/
│   └── agenda.md
├── week4-Data_Cleaning/
│   ├── Candy_Template.ipynb
│   ├── README.md
│   ├── candyhierarchy2017.xlsx
│   ├── cleaned_candy_data.csv
│   ├── cleaned_candy_ratings.csv
│   └── cleaned_merged_candy_data.csv
├── week5-Matplotlib/
│   ├── Airline.csv
│   ├── Airline.ipynb
│   └── README.md
└── week6-Seaborn/
    ├── README.md
    ├── movies.ipynb
    └── mymoviedb.csv
```

## Weekly Breakdown

| Week | Topic | Description |
|---|---|---|
| **week1-Numpy** | NumPy Fundamentals | Introductory exercises covering NumPy arrays, indexing, and vectorized operations. |
| **week2-Pandas** | Pandas Fundamentals | Working with a `students` DataFrame to practice core Pandas operations (selection, filtering, aggregation). |
| **week3-Library_Project** | Library Management Project | A small project scoped out via an agenda document, likely a library/book-tracking system exercise. |
| **week4-Data_Cleaning** | Data Cleaning | Cleans the 2017 Halloween Candy Hierarchy survey dataset — handling missing values, inconsistent text entries, and reshaping data into tidy tables. See the folder's own `README.md` for details. |
| **week5-Matplotlib** | Data Visualization with Matplotlib | Visualizes an airline dataset using Matplotlib to explore trends in the data. |
| **week6-Seaborn** | EDA with Seaborn | Exploratory data analysis on a ~9,800-movie dataset, using Seaborn to visualize popularity, ratings, genre, and language trends. See the folder's own `README.md` for details. |

## How to Use This Repo

Each week's folder is self-contained:
1. Open the week's `.ipynb` notebook in Jupyter.
2. Make sure the referenced data file(s) (CSV/XLSX) are in the same folder, or update the file path in the notebook if needed.
3. Run the notebook cells in order.
4. Check the folder's own `README.md` (where present) for a more detailed walkthrough of that week's steps.

## Requirements

Across the repo, the notebooks rely on:

```
numpy
pandas
matplotlib
seaborn
fuzzywuzzy
pycountry
```

Install everything with:
```bash
pip install numpy pandas matplotlib seaborn fuzzywuzzy pycountry
```

## Notes

- This repo is built for **educational purposes** as part of an IEEE learning track, progressing from basic Python data tools toward full exploratory data analysis workflows.
- Some subfolder details (weeks 1, 2, 3, and 5) are summarized here from folder/file names alone — check each folder's own README or notebook for the authoritative walkthrough.
