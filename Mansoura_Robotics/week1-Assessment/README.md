# Python Assessment Projects

This repository contains three small Python projects completed as practice/assessment exercises. Each project focuses on a different core skill: plain Python data structures, NumPy array operations, and Pandas-based data management with a CLI interface.

---

## 1. Student Score System
**File:** `Student_Score_System.py`

A simple console program that collects student names and grades, then reports pass/fail status for each student.

### Features
- Takes input for 3 students' names and grades
- Stores data in a dictionary (`name -> grade`)
- Classifies each student as **Passed** (grade ≥ 60) or **Failed**
- Builds a dictionary of only the students who passed
- Extracts the set of unique grades entered

### Concepts practiced
- Lists and dictionaries
- Loops and conditionals
- User input handling (`input()`, type casting)
- Sets for uniqueness

### How to run
```bash
python Student_Score_System.py
```
You will be prompted to enter 3 student names, then a grade for each.

---

## 2. Small Electronics Store (NumPy)
**File:** `small_electronics_store.py`

Analyzes sales data for a small electronics store using NumPy arrays — computing monthly revenue, total revenue per product, and identifying top performers.

### Features
- Stores units sold per product across 3 months (Jan, Feb, Mar) as a 2D array
- Calculates monthly revenue (`units_sold * price_per_unit`) using broadcasting
- Computes total revenue per product
- Finds the product with the highest total revenue
- Filters products that generated more than $15,000 in total revenue
- Finds the best-selling month for a specific product (Keyboard) and its revenue

### Concepts practiced
- NumPy array creation and shapes
- Reshaping arrays for broadcasting
- Aggregation (`.sum()`, `.argmax()`, `.max()`)
- Boolean masking / filtering

### How to run
```bash
python small_electronics_store.py
```
Requires NumPy:
```bash
pip install numpy
```

---

## 3. Student Management System (Pandas)
**File:** `Student_Management_System.py`

An interactive, menu-driven CLI application for managing student records using a Pandas DataFrame, supporting full CRUD operations.

### Features
- **Add Student** – add a new record (prevents duplicate names)
- **Search Student** – look up a student by name (case-insensitive, whitespace-trimmed)
- **Update Student Grade** – update an existing student's grade
- **Delete Student** – remove a student record
- **Show All Students** – display the full dataset
- Runs in a loop with a numbered menu until the user chooses to exit

### Concepts practiced
- Pandas DataFrames (creation, filtering, concatenation, `.loc`, `.drop`)
- String cleaning (`.str.strip()`, `.str.lower()`) for robust matching
- Building an interactive menu-driven CLI
- Input validation and error handling (`try/except`)

### How to run
```bash
python Student_Management_System.py
```
Requires Pandas:
```bash
pip install pandas
```

---

## Requirements
- Python 3.x
- `numpy` (for the electronics store project)
- `pandas` (for the student management project)

Install all dependencies at once:
```bash
pip install numpy pandas
```

## Purpose
These projects were built as hands-on practice exercises to demonstrate core Python skills, basic data analysis with NumPy, and data manipulation with Pandas in the context of small, self-contained console applications.
