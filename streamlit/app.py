import streamlit as st
import pandas as pd
from database import get_engine
import queries as q
import utils as u

st.set_page_config(page_title="Cart2Insights Dashboard", layout="wide")

engine = get_engine()

def run_query(query_func):
    return pd.read_sql(query_func(), con=engine)

st.title("🛒 Cart2Insights: Decoding E-Commerce Performance")

section = st.sidebar.radio(
    "Navigate",
    ["Business Overview", "Sales Analysis", "Customer Analysis", 
     "Seller & Product Analysis", "Delivery Analysis", "Customer Experience"]
)

if section == "Business Overview":
    st.header("📊 Business Overview")
    df = run_query(q.get_business_overview)
    row = df.iloc[0]

    col1, col2, col3 = st.columns(3)
    col1.metric("Total Revenue", u.format_currency(row["total_revenue"]))
    col2.metric("Total Orders", u.format_number(row["total_orders"]))
    col3.metric("Total Customers", u.format_number(row["total_customers"]))

    col4, col5, col6 = st.columns(3)
    col4.metric("Total Sellers", u.format_number(row["total_sellers"]))
    col5.metric("Avg Order Value", u.format_currency(row["avg_order_value"]))
    col6.metric("Avg Review Score", u.format_rating(row["avg_review_score"]))

elif section == "Sales Analysis":
    st.header("💰 Sales Analysis")

    st.subheader("Monthly Revenue Trend")
    df1 = run_query(q.get_monthly_revenue_trend)
    st.line_chart(df1.set_index("month"))

    st.subheader("Revenue by Category")
    df2 = run_query(q.get_revenue_by_category)
    st.bar_chart(df2.set_index("product_category_name"))

    st.subheader("Top-Selling Products")
    df3 = run_query(q.get_top_selling_products)
    st.dataframe(df3, width='stretch')

    st.subheader("Sales by Location")
    df4 = run_query(q.get_sales_by_location)
    st.bar_chart(df4.set_index("customer_state"))

elif section == "Customer Analysis":
    st.header("👥 Customer Analysis")

    st.subheader("Customer Distribution by State")
    df1 = run_query(q.get_customer_distribution)
    st.bar_chart(df1.set_index("customer_state"))

    st.subheader("Customer Spending Distribution")
    df2 = run_query(q.get_customer_spending)
    st.bar_chart(df2["total_spending"].value_counts(bins=20).sort_index())

    st.subheader("Repeat vs New Customers")
    df3 = run_query(q.get_repeat_vs_new)
    st.bar_chart(df3.set_index("customer_type"))

    st.subheader("Top 10 Customers by Spending")
    df4 = run_query(q.get_top_customers)
    st.dataframe(df4, width='stretch')

elif section == "Seller & Product Analysis":
    st.header("🏪 Seller & Product Analysis")

    st.subheader("Top Sellers by Revenue")
    df1 = run_query(q.get_top_sellers)
    st.dataframe(df1, width='stretch')

    st.subheader("Category Performance")
    df2 = run_query(q.get_category_performance)
    st.bar_chart(df2.set_index("product_category_name")["total_sales"])

    st.subheader("Top-Rated Sellers (min 10 reviews)")
    df3 = run_query(q.get_seller_ratings)
    st.dataframe(df3, width='stretch')

elif section == "Delivery Analysis":
    st.header("🚚 Delivery Analysis")

    df1 = run_query(q.get_avg_delivery_time)
    st.metric("Average Delivery Time", u.format_days(df1.iloc[0]["avg_delivery_days"]))

    st.subheader("On-Time vs Delayed Orders")
    df2 = run_query(q.get_ontime_vs_delayed)
    st.bar_chart(df2.set_index("delivery_status"))

    st.subheader("Average Delivery Time by State")
    df3 = run_query(q.get_delivery_by_location)
    st.bar_chart(df3.set_index("customer_state"))

    st.subheader("Delivery Delay vs Average Review Score")
    df4 = run_query(q.get_delay_vs_review)
    st.bar_chart(df4.set_index("delivery_status"))

elif section == "Customer Experience":
    st.header("⭐ Customer Experience")

    st.subheader("Review Score Distribution")
    df1 = run_query(q.get_review_score_distribution)
    st.bar_chart(df1.set_index("review_score"))

    st.subheader("Average Review Score by Category")
    df2 = run_query(q.get_reviews_by_category)
    st.bar_chart(df2.set_index("product_category_name"))

    st.subheader("Rating vs Delivery Time")
    df3 = run_query(q.get_rating_vs_delivery)
    st.bar_chart(df3.set_index("review_score"))