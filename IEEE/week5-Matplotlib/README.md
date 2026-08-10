# Airline Passenger Satisfaction — Exploratory Data Analysis

This notebook (`Untitled13.ipynb`) performs exploratory data analysis (EDA) on an airline passenger satisfaction dataset, cleaning the data and visualizing key patterns in customer demographics, travel details, and service ratings.

## Data

- **Input file:** `train.csv` (expected at `/content/train.csv`, i.e. a Google Colab environment)
- The dataset contains passenger records with fields such as `satisfaction`, `Customer Type`, `Class`, `Gender`, `Type of Travel`, `Age`, `Flight Distance`, delay times, and multiple service rating columns (wifi, food, seat comfort, boarding, entertainment, etc.)

## Requirements

```
pandas
matplotlib
numpy
```

## What the notebook does

1. **Data loading & cleaning**
   - Loads `train.csv` into a DataFrame
   - Drops the redundant `Unnamed: 0` index column
   - Checks for missing values and fills missing `Arrival Delay in Minutes` values with the column median

2. **Categorical distributions** (combined into one 2×3 grid of bar charts)
   - Customer satisfaction distribution
   - Customer type distribution (loyal vs. disloyal)
   - Class distribution (Economy, Business, Eco Plus)
   - Gender distribution
   - Type of travel distribution (business vs. personal)
   - Departure/Arrival time convenience rating

3. **Numeric distributions**
   - Age distribution (histogram with mean line)
   - Flight distance distribution (histogram with mean line)

4. **Satisfaction breakdown**
   - Pie chart of overall satisfaction percentage

5. **Delay relationship**
   - Scatter plot of departure delay vs. arrival delay

6. **Service quality analysis**
   - Average service rating by travel class (bar chart)
   - Average rating per individual service category, sorted and plotted as a horizontal bar chart

## How to run

1. Place `train.csv` in the working directory (update the path in the second cell if not using Colab's `/content/` path)
2. Run all cells top to bottom in Jupyter or Google Colab

## Output

A series of inline plots summarizing passenger demographics, travel patterns, and satisfaction drivers — useful as a first-pass exploratory analysis before building a predictive model for customer satisfaction.
