"""
Aggregation functions for expense analysis.
"""

import pandas as pd

def total_spent(df):
    """Return total amount spent."""
    return df['Amount'].sum()

def spending_by_category(df):
    """Return DataFrame with total and percentage per category."""
    cat_summary = df.groupby('Category')['Amount'].agg(['sum', 'count']).reset_index()
    cat_summary.columns = ['Category', 'Total_Spent', 'Transaction_Count']
    total = cat_summary['Total_Spent'].sum()
    cat_summary['Percentage'] = (cat_summary['Total_Spent'] / total * 100).round(2)
    cat_summary = cat_summary.sort_values('Total_Spent', ascending=False)
    return cat_summary

def monthly_spending_trend(df):
    """Return monthly total spending."""
    monthly = df.groupby(df['Date'].dt.to_period('M'))['Amount'].sum().reset_index()
    monthly['Date'] = monthly['Date'].astype(str)  # Convert Period to string for Plotly
    monthly.columns = ['Month', 'Total_Spent']
    return monthly

def payment_mode_analysis(df):
    """Return spending distribution by payment method."""
    pay_summary = df.groupby('Payment_Mode')['Amount'].agg(['sum', 'count']).reset_index()
    pay_summary.columns = ['Payment_Mode', 'Total_Spent', 'Transaction_Count']
    total = pay_summary['Total_Spent'].sum()
    pay_summary['Percentage'] = (pay_summary['Total_Spent'] / total * 100).round(2)
    return pay_summary

def top_expenses(df, n=5):
    """Return n highest individual expenses."""
    return df.nlargest(n, 'Amount')[['Date', 'Category', 'Amount', 'Payment_Mode']]

def daily_average_spend(df):
    """Calculate average daily spend (only on days with transactions)."""
    daily_totals = df.groupby('Date')['Amount'].sum()
    return daily_totals.mean()

def month_over_month_change(df):
    """Calculate percentage change in spending month over month."""
    monthly = monthly_spending_trend(df)
    monthly['Prev_Month'] = monthly['Total_Spent'].shift(1)
    monthly['MoM_Change_%'] = ((monthly['Total_Spent'] - monthly['Prev_Month']) / monthly['Prev_Month'] * 100).round(2)
    return monthly