"""
Expense Tracker App - Streamlit Dashboard
Run: streamlit run app.py
"""

import streamlit as st
import pandas as pd
import numpy as np
import os
import sys

# Add src to path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from data_generator import generate_expense_data
from data_processor import load_data, clean_data, add_time_features
from analysis import (
    total_spent, spending_by_category, monthly_spending_trend,
    payment_mode_analysis, top_expenses, daily_average_spend,
    month_over_month_change
)
from visualizer import (
    plot_category_pie, plot_monthly_trend, plot_payment_mode_distribution,
    plot_cumulative_spending, plot_weekly_heatmap
)

# Page config
st.set_page_config(
    page_title="Expense Tracker Pro",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Title
st.title("💰 Expense Tracker & Analyzer")
st.markdown("### *Data Science for Personal Finance*")

# Sidebar
st.sidebar.header("Controls")

# Option to upload file or generate synthetic data
data_option = st.sidebar.radio(
    "Choose data source:",
    ("Generate Synthetic Data", "Upload CSV")
)

df = None
if data_option == "Generate Synthetic Data":
    num_records = st.sidebar.slider("Number of records", 100, 1000, 300)
    start_date = st.sidebar.date_input("Start date", pd.to_datetime("2024-01-01"))
    end_date = st.sidebar.date_input("End date", pd.to_datetime("2024-06-30"))
    if st.sidebar.button("Generate Data"):
        with st.spinner("Generating realistic expense data..."):
            df = generate_expense_data(
                num_records=num_records,
                start_date=start_date.strftime('%Y-%m-%d'),
                end_date=end_date.strftime('%Y-%m-%d')
            )
        st.success(f"Generated {len(df)} expense records!")
else:
    uploaded_file = st.sidebar.file_uploader("Choose a CSV file", type="csv")
    if uploaded_file is not None:
        df = load_data(uploaded_file)
        st.success("File uploaded successfully!")

if df is not None:
    # Clean and process
    df_clean = clean_data(df)
    df_feat = add_time_features(df_clean)
    
    # Sidebar filters
    st.sidebar.subheader("Filters")
    categories = ['All'] + list(df_feat['Category'].unique())
    selected_category = st.sidebar.selectbox("Select Category", categories)
    
    payment_modes = ['All'] + list(df_feat['Payment_Mode'].unique())
    selected_payment = st.sidebar.selectbox("Select Payment Mode", payment_modes)
    
    # Apply filters
    df_filtered = df_feat.copy()
    if selected_category != 'All':
        df_filtered = df_filtered[df_filtered['Category'] == selected_category]
    if selected_payment != 'All':
        df_filtered = df_filtered[df_filtered['Payment_Mode'] == selected_payment]
    
    # Main dashboard
    col1, col2, col3, col4 = st.columns(4)
    total = total_spent(df_filtered)
    avg_daily = daily_average_spend(df_filtered)
    num_trans = len(df_filtered)
    top_cat = spending_by_category(df_filtered).iloc[0]['Category'] if not df_filtered.empty else "N/A"
    
    col1.metric("Total Spent", f"₹{total:,.2f}")
    col2.metric("Avg Daily Spend", f"₹{avg_daily:,.2f}")
    col3.metric("Transactions", num_trans)
    col4.metric("Top Category", top_cat)
    
    # Tabs for different views
    tab1, tab2, tab3, tab4 = st.tabs(["📊 Overview", "📈 Trends", "💳 Payment Analysis", "🔍 Raw Data"])
    
    with tab1:
        st.subheader("Category-wise Spending")
        cat_summary = spending_by_category(df_filtered)
        col_left, col_right = st.columns([1, 1])
        with col_left:
            fig_pie = plot_category_pie(cat_summary)
            st.plotly_chart(fig_pie, use_container_width=True)
        with col_right:
            st.dataframe(cat_summary.style.format({"Total_Spent": "₹{:,.2f}", "Percentage": "{:.2f}%"}))
        
        st.subheader("Top Expenses")
        top_exp = top_expenses(df_filtered, 10)
        st.dataframe(top_exp.style.format({"Amount": "₹{:,.2f}"}))
    
    with tab2:
        st.subheader("Monthly Spending Trend")
        monthly = monthly_spending_trend(df_filtered)
        fig_bar = plot_monthly_trend(monthly)
        st.plotly_chart(fig_bar, use_container_width=True)
        
        st.subheader("Month-over-Month Change")
        mom = month_over_month_change(df_filtered)
        st.dataframe(mom.style.format({"Total_Spent": "₹{:,.2f}", "Prev_Month": "₹{:,.2f}", "MoM_Change_%": "{:.2f}%"}))
        
        st.subheader("Cumulative Spending")
        fig_cum = plot_cumulative_spending(df_filtered)
        st.plotly_chart(fig_cum, use_container_width=True)
        
        st.subheader("Weekly Spending Heatmap")
        fig_heat = plot_weekly_heatmap(df_feat)  # Use full data for heatmap
        st.plotly_chart(fig_heat, use_container_width=True)
    
    with tab3:
        st.subheader("Payment Mode Distribution")
        pay_summary = payment_mode_analysis(df_filtered)
        col1, col2 = st.columns([1, 1])
        with col1:
            fig_pay = plot_payment_mode_distribution(pay_summary)
            st.plotly_chart(fig_pay, use_container_width=True)
        with col2:
            st.dataframe(pay_summary.style.format({"Total_Spent": "₹{:,.2f}", "Percentage": "{:.2f}%"}))
    
    with tab4:
        st.subheader("Filtered Expense Data")
        st.dataframe(df_filtered)
        
        # Download button
        csv = df_filtered.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="Download filtered data as CSV",
            data=csv,
            file_name='expenses_filtered.csv',
            mime='text/csv',
        )
    
    # Insights section (dynamic)
    st.markdown("---")
    st.subheader("📌 Key Insights")
    cat_summary_all = spending_by_category(df_feat)
    top_cat_name = cat_summary_all.iloc[0]['Category']
    top_cat_pct = cat_summary_all.iloc[0]['Percentage']
    
    st.write(f"🔹 Your highest spending category is **{top_cat_name}** which accounts for **{top_cat_pct}%** of total expenses.")
    
    monthly_all = monthly_spending_trend(df_feat)
    if len(monthly_all) >= 2:
        last_month = monthly_all.iloc[-1]['Total_Spent']
        prev_month = monthly_all.iloc[-2]['Total_Spent']
        if last_month > prev_month:
            st.write(f"🔹 Spending increased by **₹{last_month - prev_month:,.2f}** compared to previous month.")
        else:
            st.write(f"🔹 Spending decreased by **₹{prev_month - last_month:,.2f}** compared to previous month.")
    
    pay_summary_all = payment_mode_analysis(df_feat)
    top_pay = pay_summary_all.iloc[0]['Payment_Mode']
    top_pay_pct = pay_summary_all.iloc[0]['Percentage']
    st.write(f"🔹 Most used payment method is **{top_pay}** ({top_pay_pct}% of total).")
    
else:
    st.info("👈 Please generate synthetic data or upload a CSV file from the sidebar to begin analysis.")

# Footer
st.markdown("---")
st.markdown("Built with ❤️ using Streamlit, Pandas, and Plotly | [GitHub Repository](https://github.com/yourusername/Expense-Tracker-App)")