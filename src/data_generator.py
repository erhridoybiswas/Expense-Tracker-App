"""
Generate synthetic expense data for the Expense Tracker App.
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

def generate_expense_data(
    num_records=300,
    start_date='2024-01-01',
    end_date='2024-06-30',
    seed=42
):
    """
    Generate synthetic expense records with realistic patterns.
    
    Parameters:
    - num_records: total number of expense entries
    - start_date, end_date: date range
    - seed: for reproducibility
    
    Returns:
    - DataFrame with columns: Date, Category, Amount, Payment_Mode, Description
    """
    np.random.seed(seed)
    random.seed(seed)
    
    # Date range
    start = datetime.strptime(start_date, '%Y-%m-%d')
    end = datetime.strptime(end_date, '%Y-%m-%d')
    date_list = [start + timedelta(days=random.randint(0, (end-start).days)) 
                 for _ in range(num_records)]
    
    # Categories with realistic probabilities
    categories = {
        'Food': 0.25,
        'Transport': 0.15,
        'Shopping': 0.18,
        'Entertainment': 0.12,
        'Bills': 0.15,
        'Healthcare': 0.05,
        'Education': 0.05,
        'Other': 0.05
    }
    
    cat_choices = np.random.choice(
        list(categories.keys()),
        size=num_records,
        p=list(categories.values())
    )
    
    # Amount generation based on category (realistic ranges in INR)
    amount_ranges = {
        'Food': (50, 800),
        'Transport': (20, 500),
        'Shopping': (100, 5000),
        'Entertainment': (100, 2000),
        'Bills': (500, 3000),
        'Healthcare': (200, 3000),
        'Education': (500, 5000),
        'Other': (50, 1500)
    }
    
    amounts = []
    for cat in cat_choices:
        low, high = amount_ranges[cat]
        amounts.append(round(np.random.uniform(low, high), 2))
    
    # Payment modes
    payment_modes = ['Cash', 'Credit Card', 'Debit Card', 'UPI', 'Net Banking']
    pay_probs = [0.2, 0.3, 0.2, 0.25, 0.05]
    payment_mode = np.random.choice(payment_modes, size=num_records, p=pay_probs)
    
    # Description (optional)
    descriptions = [f"Expense for {cat}" for cat in cat_choices]
    
    df = pd.DataFrame({
        'Date': date_list,
        'Category': cat_choices,
        'Amount': amounts,
        'Payment_Mode': payment_mode,
        'Description': descriptions
    })
    
    # Sort by date
    df = df.sort_values('Date').reset_index(drop=True)
    
    return df

if __name__ == "__main__":
    # Test generation
    df = generate_expense_data(300)
    print(df.head())
    df.to_csv('data/raw/expenses_synthetic.csv', index=False)
    print("Synthetic data saved to data/raw/expenses_synthetic.csv")