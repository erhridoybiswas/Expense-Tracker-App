"""
Data cleaning and preprocessing functions.
"""

import pandas as pd
import numpy as np

def load_data(filepath):
    """Load CSV into DataFrame with proper date parsing."""
    df = pd.read_csv(filepath, parse_dates=['Date'])
    return df

def clean_data(df):
    """
    Perform cleaning operations:
    - Remove duplicates
    - Handle missing values
    - Standardize category names (strip whitespace, title case)
    - Ensure amount is positive
    """
    df_clean = df.copy()
    
    # Remove exact duplicates
    df_clean = df_clean.drop_duplicates()
    
    # Drop rows where Amount is NaN or zero/negative
    df_clean = df_clean.dropna(subset=['Amount'])
    df_clean = df_clean[df_clean['Amount'] > 0]
    
    # Standardize category names
    df_clean['Category'] = df_clean['Category'].str.strip().str.title()
    
    # Standardize Payment Mode
    df_clean['Payment_Mode'] = df_clean['Payment_Mode'].str.strip().str.title()
    
    # Convert date to datetime (already done if using parse_dates)
    df_clean['Date'] = pd.to_datetime(df_clean['Date'])
    
    return df_clean

def add_time_features(df):
    """Add month, year, day of week, week number for analysis."""
    df_feat = df.copy()
    df_feat['Month'] = df_feat['Date'].dt.month
    df_feat['Year'] = df_feat['Date'].dt.year
    df_feat['Month_Name'] = df_feat['Date'].dt.strftime('%B')
    df_feat['YearMonth'] = df_feat['Date'].dt.to_period('M')
    df_feat['Day_of_Week'] = df_feat['Date'].dt.day_name()
    df_feat['Week_Number'] = df_feat['Date'].dt.isocalendar().week
    return df_feat

if __name__ == "__main__":
    # Test pipeline
    df_raw = load_data('../data/raw/expenses_synthetic.csv')
    df_clean = clean_data(df_raw)
    df_final = add_time_features(df_clean)
    print(df_final.info())
    df_final.to_csv('../data/processed/expenses_clean.csv', index=False)