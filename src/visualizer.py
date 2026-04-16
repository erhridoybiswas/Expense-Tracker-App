"""
Create Plotly charts for Streamlit.
"""

import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

def plot_category_pie(cat_summary_df):
    """Pie chart of spending by category."""
    fig = px.pie(
        cat_summary_df,
        values='Total_Spent',
        names='Category',
        title='Spending by Category',
        hole=0.3,  # Donut style
        color_discrete_sequence=px.colors.qualitative.Set3
    )
    fig.update_traces(textposition='inside', textinfo='percent+label')
    return fig

def plot_monthly_trend(monthly_df):
    """Bar chart of monthly spending."""
    fig = px.bar(
        monthly_df,
        x='Month',
        y='Total_Spent',
        title='Monthly Spending Trend',
        labels={'Total_Spent': 'Amount (₹)', 'Month': 'Month'},
        text_auto='.2s',
        color='Total_Spent',
        color_continuous_scale='Blues'
    )
    fig.update_layout(xaxis_tickangle=-45)
    return fig

def plot_payment_mode_distribution(pay_df):
    """Horizontal bar chart for payment modes."""
    fig = px.bar(
        pay_df,
        y='Payment_Mode',
        x='Total_Spent',
        title='Spending by Payment Mode',
        orientation='h',
        text='Percentage',
        color='Total_Spent',
        color_continuous_scale='Viridis'
    )
    fig.update_traces(texttemplate='%{text}%', textposition='outside')
    return fig

def plot_cumulative_spending(df):
    """Line chart of cumulative spending over time."""
    df_sorted = df.sort_values('Date')
    df_sorted['Cumulative'] = df_sorted['Amount'].cumsum()
    fig = px.line(
        df_sorted,
        x='Date',
        y='Cumulative',
        title='Cumulative Spending Over Time',
        labels={'Cumulative': 'Cumulative Amount (₹)'}
    )
    return fig

def plot_weekly_heatmap(df):
    """Heatmap of spending by day of week vs week number."""
    pivot = df.pivot_table(
        values='Amount',
        index='Day_of_Week',
        columns='Week_Number',
        aggfunc='sum',
        fill_value=0
    )
    # Reorder days
    days_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    pivot = pivot.reindex(days_order)
    
    fig = go.Figure(data=go.Heatmap(
        z=pivot.values,
        x=pivot.columns,
        y=pivot.index,
        colorscale='YlOrRd',
        hoverongaps=False))
    fig.update_layout(title='Weekly Spending Heatmap (Week Number vs Day)',
                      xaxis_title='Week Number',
                      yaxis_title='Day of Week')
    return fig