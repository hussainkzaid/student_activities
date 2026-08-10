# Library Management Analysis

A data analysis project exploring how a local library's books are borrowed, using three related datasets covering books, members, and borrowing records. The goal is to surface patterns in borrowing behavior and produce insights the library can use to improve its collection and services.

## Project overview

The analysis answers questions such as:

- What's the probability of randomly selecting a borrowed book from a given genre, a member of a given membership type, or a borrowing record matching two conditions?
- Which genres, authors, and members are most and least active in terms of borrowing?
- How does borrowing activity vary by membership type, publication year, and month?
- Which books have never been borrowed, and how does borrowing duration vary by genre?
- What does the distribution of books across genres look like, and what other patterns stand out (age groups, page counts, copies available)?
- What numerical insights can NumPy provide on top of the Pandas analysis (max/min values, filtering, sorting, vectorized calculations)?

All of this is done using **Pandas** for data manipulation/aggregation and **NumPy** for array-based numerical analysis. The notebook ends with a final summary cell that pulls the most important findings together into a small set of actionable recommendations for the library.

## Dataset

The analysis uses three CSV files:

| File | Rows | Description |
|---|---|---|
| `books.csv` | 400 | Book catalog: `BookID`, `Title`, `Author`, `Genre`, `PublicationYear`, `Publisher`, `Pages`, `Language`, `CopiesAvailable` |
| `borrowings.csv` | 2,000 | Borrowing records: `BorrowID`, `MemberID`, `BookID`, `BorrowDate`, `ReturnDate` |
| `members.csv` | 150 | Library members: `MemberID`, `Name`, `MembershipType`, `Age`, `Gender`, `JoinDate` |

These three tables are merged on `BookID` and `MemberID` to build combined views (e.g. borrowings joined with book details, borrowings joined with member details) used throughout the analysis.

**Note on data quality:** the dataset is used largely as-is. No full cleaning pass was performed, since the task only calls for minimal fixes needed to keep the analysis running (e.g. parsing `BorrowDate`/`ReturnDate` as datetimes where needed for date-based calculations).

## How to run

1. **Get the files**: place `books.csv`, `borrowings.csv`, and `members.csv` in the same folder as the notebook (or update the file paths in the "load the dataset" cell if you keep them elsewhere).
2. **Install dependencies**:
   ```bash
   pip install pandas numpy jupyter
   ```
3. **Open the notebook**:
   ```bash
   jupyter notebook Library_Management_Analysis.ipynb
   ```
   (This notebook was originally developed in Google Colab. If running there instead, keep the first cell, which prompts you to upload the three CSV files interactively. If running locally/in Jupyter, you can delete or skip that cell and just make sure the CSVs are in the working directory before running the "load the dataset" cell.)
4. **Run all cells in order** (`Run All` / `Cell > Run All`). The notebook is self-contained — each section builds on the dataframes and merged tables created earlier, so cells should be executed top to bottom rather than out of order.
5. **Read the final summary**: the last markdown cell in the notebook summarizes the key findings and recommendations without needing to re-run anything.

## Project structure

```
.
├── README.md                          # This file
├── Library_Management_Analysis.ipynb  # Main analysis notebook
├── books.csv                          # Book catalog (not included — supply your own)
├── borrowings.csv                     # Borrowing records (not included — supply your own)
└── members.csv                        # Member records (not included — supply your own)
```

## Key findings (short version)

- **Mystery is the most-borrowed genre** (512 borrowings) despite Business having the largest catalog (52 books) — a sign that the library's stock doesn't fully match reader demand.
- **23 of 400 books have never been borrowed**, suggesting some titles need promotion or reconsideration.
- **Students account for ~60% of all borrowings**, in line with their share of total membership.
- **Borrowing peaks in March and dips sharply by September** (~47% drop), pointing to a seasonal pattern worth planning around.

See the final summary cell in the notebook for the full breakdown and recommendations.
