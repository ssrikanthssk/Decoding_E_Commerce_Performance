# Cart2Insights: Decoding E-Commerce Performance

## Project Objective

An e-commerce platform generates large volumes of data across orders, products, sellers, payments, deliveries, and customer reviews — spread across multiple related datasets. This project analyzes that data end-to-end to uncover meaningful business insights related to sales, customers, products, sellers, payments, delivery performance, and customer satisfaction, and presents them through an interactive dashboard.

**Domain:** E-Commerce & Retail Analytics

## Business Use Cases

- E-Commerce Performance Monitoring
- Customer Behavior & Segmentation
- Sales & Revenue Optimization
- Product & Seller Performance Analysis
- Delivery & Operational Optimization
- Customer Experience Improvement
- Data-Driven Business Decision Making

## Tech Stack

Python, Pandas, SQL (MySQL), SQLAlchemy, Streamlit, Matplotlib/Seaborn/Plotly, SciPy (statistical testing)

## Approach / Workflow

1. **Business Understanding** — defined objectives and key analysis questions.
2. **Data Understanding & ER Diagram** — explored 9 related tables, identified keys and relationships, built a data dictionary.
3. **Data Loading** — loaded all raw CSVs with Pandas, checked shape/columns/dtypes.
4. **Data Quality Analysis** — identified missing values, duplicates, invalid/inconsistent values, outliers, and PK uniqueness issues.
5. **Data Cleaning & Preprocessing** — handled missing values, removed duplicates, corrected data types, formatted dates, standardized categories.
6. **SQL Database** — created the database and tables per the ER diagram, loaded cleaned data, applied PK/FK constraints.
7. **Feature Engineering** — created business features: total order value, delivery days, delivery delay, customer order count & spend, average order value, seller revenue/order count, repeat customer indicator.
8. **Exploratory Data Analysis** — univariate, bivariate, multivariate, trend, correlation, and distribution analysis.
9. **Statistical Analysis** — hypothesis testing (T-Test, ANOVA, Chi-Square) to validate business questions.
10. **SQL Analysis & Streamlit Dashboard** — built an interactive dashboard covering Business Overview, Sales, Customers, Sellers/Products, Delivery, and Customer Experience.
11. **Business Insights** — translated statistical findings into Observation → Interpretation → Business Impact recommendations.

## Project Structure

```
data/
  raw/
  cleaned/
notebooks/
  01_data_understanding.ipynb
  02_data_quality_analysis.ipynb
  03_data_cleaning.ipynb
  04_sql_analysis.ipynb
  05_feature_engineering.ipynb
  06_eda.ipynb
  07_statistical_analysis.ipynb
  08_business_insights.ipynb
streamlit/
  app.py
  database.py
  queries.py
  utils.py
README.md
requirements.txt
```

## Setup Instructions

1. Clone the repository
   ```
   git clone <your-repo-url>
   cd cart2insights
   ```
2. Create a virtual environment and install dependencies
   ```
   python -m venv venv
   source venv/bin/activate   # on Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```
3. Set up the MySQL database and update connection details via environment variables (do **not** hardcode credentials):
   ```
   DB_HOST=localhost
   DB_USER=your_user
   DB_PASSWORD=your_password
   DB_NAME=cart2insights
   ```
4. Run the notebooks in order (01 → 08) to reproduce data cleaning, loading, feature engineering, EDA, and statistical analysis.
5. Launch the dashboard
   ```
   cd streamlit
   streamlit run app.py
   ```

## Statistical Analysis Summary

| Test | Question | Result |
|---|---|---|
| Independent T-Test | Do delayed orders get lower review scores? | Significant (p < 0.001); delayed avg 2.57 vs on-time avg 4.29 |
| One-Way ANOVA | Does order value differ across product categories? | Significant (F = 212.45, p < 0.001) |
| Chi-Square | Is payment method associated with order status? | Significant (p < 0.001); boleto linked to higher cancellations |

## Business Insights & Recommendations

### 1. Delivery Delay Is the #1 Driver of Dissatisfaction
**Observation:** Delayed orders average a 2.57 review score vs. 4.29 for on-time orders (t-test, p < 0.001).
**Interpretation:** Delivery speed has by far the strongest relationship with customer satisfaction, more than price, product type, or payment method.
**Business Impact:** Prioritize carrier reliability and proactive delay notifications — this is the single highest-leverage lever for improving satisfaction scores.

### 2. Product Category Drives Order Value Significantly
**Observation:** ANOVA shows significant differences in average order value across 66 categories (F = 212.45, p < 0.001); computers (pcs) lead at ~R$1,098 avg.
**Interpretation:** High-ticket categories (electronics, appliances) contribute disproportionately to revenue per order.
**Business Impact:** Focus marketing spend and inventory investment on high-value categories to maximize revenue per transaction.

### 3. Boleto Payments Show Higher Cancellation Risk
**Observation:** Chi-square confirms payment method is significantly associated with order status (p < 0.001); boleto has a relatively higher share of canceled orders than credit card or voucher.
**Interpretation:** Boleto's delayed/manual payment confirmation likely causes some orders to lapse before payment completes.
**Business Impact:** Add payment reminders or shorten the boleto payment window to reduce cancellations.

### 4. Revenue Growth Is Steady but Delivery Has a Long-Tail Risk
**Observation:** Monthly revenue grew steadily from late 2016 through 2018; delivery time is right-skewed with a median around 10 days but a tail out to 200 days.
**Interpretation:** While overall growth is healthy, a subset of orders face severe logistics delays that likely drive the 1-star review cluster.
**Business Impact:** Investigate root causes for extreme-delay outliers (specific regions/carriers) as a targeted operational fix.

### 5. Regional Disparity in Satisfaction and Delivery
**Observation:** Average review scores vary by state (3.6–4.2), with remote states (e.g. RR) scoring lowest.
**Interpretation:** Delivery infrastructure gaps in remote regions likely translate directly into lower satisfaction.
**Business Impact:** Consider regional carrier partnerships or adjusted delivery estimates for underserved states to manage expectations.

## Dashboard Overview

The Streamlit dashboard is organized into 6 sections:

1. **Business Overview** — Total Revenue, Orders, Customers, Sellers, AOV, Avg Review Score
2. **Sales Analysis** — Monthly revenue trend, revenue by category, top-selling products, sales by location
3. **Customer Analysis** — Customer distribution, spending, repeat vs new customers, top customers
4. **Seller & Product Analysis** — Top sellers, seller revenue, category performance, seller ratings
5. **Delivery Analysis** — Avg delivery time, on-time vs delayed orders, delivery by location, delay vs review score
6. **Customer Experience** — Review score distribution, reviews by category, rating vs delivery performance

## Results

This project delivers an end-to-end e-commerce data analytics solution — from raw data to a cleaned SQL database, statistically validated findings, and an interactive dashboard — translating data into actionable business recommendations.

## Author

Project by Srikanth S
