# Candy Hierarchy 2017 — Data Cleaning Project

An educational data-wrangling project that takes the raw **Boing Boing Halloween Candy Hierarchy 2017** survey and cleans it into tidy, analysis-ready tables.

## Contents

| File | Description |
|---|---|
| `Candy_Template.ipynb` | Jupyter notebook containing the full data wrangling walkthrough |
| `candyhierarchy2017.xlsx` | Raw source dataset (2,460 rows × 120 columns) |
| `cleaned_candy_data.csv` | Cleaned respondent-level table (1,798 rows × 10 columns) |
| `cleaned_candy_ratings.csv` | Cleaned candy ratings in long format (185,194 rows × 3 columns) |
| `cleaned_merged_candy_data.csv` | Respondent data merged with candy ratings (185,194 rows × 12 columns) |

## About the Dataset

The raw survey asks respondents about Halloween habits and has them rate ~100 individual candies as **Joy**, **Meh**, or **Despair**. Key raw fields include:

- **Q1: Going Out?** — Yes/No
- **Q2: Gender** — Female / Male / Other / I'd rather not say
- **Q3: Age** — free-text numeric field
- **Q4: Country** — free-text, inconsistently written (e.g. "USA", "us", "America")
- **Q5: State/Province/County** — free-text region
- **Q6 [Candy Name]** — one column per candy, rated Joy / Meh / Despair
- **Q10: Dress** — color perception question
- **Q11: Day** — Halloween day/date question
- **Q12: Media** — four separate Yes/No columns (Yahoo, Daily Dish, ESPN, Science)

## Cleaning Steps (Notebook Walkthrough)

1. **Load data** from the raw Excel file.
2. **Inspect** structure, data types, and missing values.
3. **Consolidate media columns** — merged the four `Q12: MEDIA` yes/no columns into a single `Media` column (`Unknown` where none were marked).
4. **Drop unusable columns/rows** — removed mostly-empty columns (`Internal ID` metadata, `Q9: OTHER COMMENTS`, despair/joy "other" free-text) and rows with excessive missing data.
5. **Clean "Going Out?"** — filled missing values with the column mode.
6. **Clean Gender** — filled missing values with `"I'd rather not say"`.
7. **Clean Age** — converted free-text entries (e.g. "old", "60+", joke answers) to numeric, dropped nonsensical rows, and coerced the column to a proper numeric type.
8. **Clean Country** — standardized inconsistent spellings/abbreviations using `fuzzywuzzy` and `pycountry`, filled missing values with `"Unknown"`.
9. **Clean Area (state/province)** — used fuzzy string matching to consolidate similar entries.
10. **Reshape candy ratings** — melted the ~100 `Q6` candy columns into a long-format table (`Internal ID`, `Candy`, `Rating`), dropping unrated entries, and separated this into its own table.
11. **Clean Dress and Day columns** — reviewed and standardized responses (e.g. unified "Unknown" day entries to the mode).
12. **Renamed columns** to friendlier lowercase names (`going out`, `gender`, `age`, `country`, `area`, `day`, `dress`).
13. **Validation** — re-checked data types, missing values, and summary statistics after cleaning.
14. **Merge** — joined the cleaned respondent table with the candy ratings table on `Internal ID` to produce a single combined dataset.
15. **Export** — saved three outputs: the cleaned respondent table, the cleaned candy ratings table, and the merged table.

## Requirements

```
pandas
numpy
fuzzywuzzy
pycountry
```

Install with:
```bash
pip install pandas numpy fuzzywuzzy pycountry
```

## Usage

Open `Candy_Template.ipynb` in Jupyter and run the cells in order. The notebook expects the raw file at `candyhierarchy2017.xlsx` and will produce the three cleaned CSVs as output.

## Notes

- This project is for **educational purposes**, focused on practicing real-world data wrangling: handling missing data, inconsistent free-text entries, reshaping wide-to-long data, and merging tables.
- Original survey data is public from Boing Boing's annual Halloween candy survey (2017 edition).
