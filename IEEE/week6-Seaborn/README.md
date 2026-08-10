# Movie Dataset — Exploratory Data Analysis

An exploratory data analysis (EDA) project that cleans and visualizes a dataset of ~9,800 movies to uncover trends in popularity, ratings, genre, language, and release year.

## Contents

| File | Description |
|---|---|
| `movies.ipynb` | Jupyter notebook containing the data cleaning and full EDA walkthrough |
| `mymoviedb.csv` | Raw source dataset (9,837 rows × 9 columns) |

## About the Dataset

Each row represents a movie, with the following fields:

- **Release_Date** — the movie's release date
- **Title** — movie title
- **Overview** — short plot summary
- **Popularity** — a popularity score
- **Vote_Count** — number of user votes
- **Vote_Average** — average user rating
- **Original_Language** — ISO language code of the movie's original language
- **Genre** — one or more comma-separated genres
- **Poster_Url** — URL to the movie's poster image

## Notebook Walkthrough

1. **Import libraries** — `pandas`, `numpy`, `matplotlib`, and `seaborn` (with the `darkgrid` style).
2. **Load the data** from `mymoviedb.csv`.
3. **Inspect structure** with `.info()` to check data types and non-null counts.
4. **Fix data types**:
   - Converted `Release_Date` to a proper datetime type.
   - Converted `Vote_Average` and `Vote_Count` to numeric types.
5. **Handle missing values** — checked null counts per column and dropped rows with missing data.
6. **Derive a `Year` column** from `Release_Date` for year-based analysis.
7. **Explode genres** — split the comma-separated `Genre` field into individual genre rows for genre-level analysis.
8. **Answer exploratory questions**, each paired with a visualization:
   - Which movies have the highest popularity, and what genres are they?
   - What year had the highest number of films produced?
   - What is the most common film genre?
   - Which genres have the highest average rating?
   - Which genres are the most/least popular on average?
   - How has the average movie rating changed over the years?
   - Which languages have the highest total popularity and highest average rating?
   - Is there a relationship between popularity and rating (scatter plot)?
   - Which movies have the highest vote averages?

## Requirements

```
pandas
numpy
matplotlib
seaborn
```

Install with:
```bash
pip install pandas numpy matplotlib seaborn
```

## Usage

Open `movies.ipynb` in Jupyter and run the cells in order. Update the file path in the second cell to point to your local copy of `mymoviedb.csv` if needed, then run the notebook to reproduce the cleaning steps and all charts.

## Notes

- This project is for **educational/portfolio purposes**, focused on practicing an end-to-end EDA workflow: type conversion, missing-value handling, feature engineering (`Year`), reshaping multi-value fields (`Genre`), and answering business-style questions with visualizations.
