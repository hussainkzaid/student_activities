# Pandas Practice Notebook

A hands-on set of pandas exercises built around a student-records dataset,
covering DataFrame creation, inspection, selection, filtering, aggregation,
missing-data handling, merging/concatenation, and exporting to CSV.

## Contents

`Pandas.ipynb` walks through the following exercises:

1. **Create a DataFrame** — build `df` from a dictionary of student names, ages, grades, and departments.
2. **Inspect the DataFrame** — view `head()`, `tail()`, `shape`, `columns`, and `dtypes`; explain the difference between `shape`, `size`, and `len(df)`.
3. **Selection & filtering** — select single/multiple columns, slice rows, and filter by conditions (e.g., grade > 85, department == "AI") using `.loc`.
4. **Add derived columns** — create a `Passed` column (`Yes`/`No` based on grade) and a `Grade_Level` column (`Excellent`/`Good`/`Average`) via `.apply()`; update a value in place with `.loc`.
5. **Aggregations** — compute average/highest/lowest grade, find the top student, and group by department for average age and student counts.
6. **Build a filtered/sorted DataFrame** — create a new DataFrame of students with grade > 80, sorted descending, with only selected columns.
7. **Handle missing data** — build `df_missing`, detect missing values with `isnull()`, and fill them (`"Unknown"` for names, column mean for numeric fields).
8. **Merge DataFrames** — combine `students_info` and `students_grades` on the `ID` column using `pd.merge()`.
9. **Concatenate DataFrames** — append new student records with `pd.concat()`.
10. **Group-by analysis** — find the average grade per department and identify the top-performing department with `idxmax()`.
11. **Export to CSV** — save the final DataFrame with `to_csv()`.

## Requirements

- Python 3
- [pandas](https://pandas.pydata.org/)
- Jupyter Notebook or JupyterLab

## Setup

```bash
pip install pandas jupyter
jupyter notebook Pandas.ipynb
```

## Topics Covered

- DataFrame creation from dictionaries
- Inspection (`head`, `tail`, `shape`, `columns`, `dtypes`)
- Indexing & filtering (`.loc`, boolean masks)
- Column creation with `.apply()`
- Aggregation (`mean`, `max`, `min`, `groupby`, `idxmax`)
- Sorting and column selection
- Missing-value detection and imputation (`isnull`, `fillna`)
- Merging (`pd.merge`) and concatenation (`pd.concat`)
- Exporting data (`to_csv`)
