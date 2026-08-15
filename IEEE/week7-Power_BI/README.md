# Telco Customer Churn Dashboard

A single-page Power BI dashboard for analyzing customer churn at a telecom company — built to surface who is churning, why, and how much revenue is at stake.

## Overview

**File:** `Telco_Customer_Churn_Dashboard.pbix`
**Tool:** Power BI Desktop
**Data source table:** `churn`

The report title reads **"Customer Retention & Churn Mitigation Dashboard"** and is laid out as one page (1280×720) containing four KPI cards, four charts, and a header textbox.

## Dashboard Contents

### KPI Cards
| Card | Metric |
|---|---|
| Total Churned Customers | Count of customers marked as churned |
| Overall Churn Rate (%) | Percentage of customers who have churned |
| Total Revenue | Sum of revenue across all customers |
| Total Lost Revenue | Revenue attributable to churned customers |

### Charts
| Visual | Type | Axes / Fields |
|---|---|---|
| Contract Type vs. Customer Status | Bar chart | Category: `Contract Type`, Series: `Customer_Status`, Value: `Customer Count` |
| Payment Method vs. Customer Status | Clustered column chart | Category: `Payment Method`, Series: `Customer_Status`, Value: Count of `Customer_ID` |
| Internet Type — Add-on Adoption | Clustered column chart | Category: `Internet Type`, Values: Count of `Online Security`, Count of `Premium Support` |
| Churn Reasons | Bar chart | Category: `Churn_Reason`, Value: Count of `Customer_ID` |
| Tenure vs. Monthly Charge | Scatter chart | X: `Monthly Charge ($)`, Y: `Tenure (Months)`, Series: `Customer_Status` |

## Key Fields Used

- `Customer_ID`
- `Customer_Status` (e.g., Churned / Stayed / Joined)
- `Contract` (Contract Type)
- `Payment_Method`
- `Internet_Type`
- `Online_Security`
- `Premium_Support`
- `Churn_Reason`
- `Monthly_Charge`
- `Tenure_in_Months`
- `Total_Revenue`

## Measures (DAX)

The following measures are defined in the data model and used across the KPI cards:

- `Total Churned Customers`
- `Overall Churn Rate (%)`
- `Total Lost Revenue`

> Note: the underlying DAX formulas are stored in the compressed Power BI data model and aren't extractable from the file listing alone — open the file in Power BI Desktop and check the **Data** pane / **Measure** editor to view or edit them.

## How to Use

1. Open `Telco_Customer_Churn_Dashboard.pbix` in **Power BI Desktop** (free download from Microsoft).
2. On open, Power BI will prompt to refresh the data connection — point it at your current `churn` data source, or refresh if the source is already configured.
3. Use the cross-filtering: clicking any bar/column/point filters the rest of the page (e.g., click "Churned" in the status legend to see churn-only breakdowns across all charts).
4. KPI cards at the top give an at-a-glance summary; the charts below drill into contract type, payment method, service add-ons, churn reasons, and the relationship between tenure and monthly charges.

## Requirements

- Power BI Desktop (Windows) to open, edit, or refresh the `.pbix` file.
- Power BI Service or Power BI mobile to view a published version, if published.

## Suggested Next Steps

- Add a second page for demographic breakdowns (gender, age, geography) if that data is available in the source.
- Add a churn-prediction visual (e.g., a table or gauge for predicted at-risk customers) if a model is layered on top of this data.
- Document the exact DAX for the three measures above directly in this README once confirmed in Power BI Desktop.
