# 💰 Expense Tracker Pro – Data Science for Personal Finance

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/yourusername/expense-tracker-app/main/app.py)
![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)

A complete, industry-ready **Expense Tracker Application** built with Python, Pandas, and Streamlit. This project demonstrates data cleaning, analysis, and interactive visualization skills essential for Data Analyst and Financial Analyst roles.

## 📌 Overview

Understanding where your money goes is the first step toward financial freedom. This app allows you to:
- **Generate realistic synthetic expense data** (no real bank data needed).
- **Upload your own CSV** for personalized analysis.
- **Explore interactive dashboards** with category breakdowns, monthly trends, and payment mode analysis.
- **Derive actionable insights** like top spending categories and month-over-month changes.

## ❓ Problem Statement

Individuals and small businesses often lack a simple yet powerful tool to track daily expenses and identify spending patterns. Manual spreadsheets are error-prone and lack visual insights. This project solves that by providing an automated, data-driven expense tracker with a user-friendly web interface.

## ✅ Solution & Features

- **Synthetic Data Generator**: Creates realistic expense records with customizable date range and volume.
- **Data Cleaning Pipeline**: Handles duplicates, missing values, and standardizes categories.
- **Advanced Analytics**: 
  - Total spend, average daily spend, transaction count.
  - Category-wise percentage distribution.
  - Monthly spending trends with MoM change.
  - Payment method preferences.
- **Interactive Visualizations** (Plotly):
  - Donut chart for category share.
  - Bar chart for monthly totals.
  - Cumulative spending line chart.
  - Weekly spending heatmap.
- **Dynamic Insights**: Automatically generated text summaries based on data.
- **Filter by Category & Payment Mode**: Drill down into specific segments.
- **Download Filtered Data**: Export as CSV for further analysis.

## 🛠 Tech Stack

| Area | Tools |
|------|-------|
| Language | Python 3.9+ |
| Data Manipulation | Pandas, NumPy |
| Visualization | Plotly Express, Matplotlib, Seaborn |
| Web Framework | Streamlit |
| Synthetic Data | Custom logic (optional Faker) |

## 📂 Project Structure
Expense-Tracker-App/
├── data/ # Raw and processed CSV files (ignored in git)
├── notebooks/ # Jupyter notebooks for EDA (optional)
├── src/ # Core modules
│ ├── data_generator.py
│ ├── data_processor.py
│ ├── analysis.py
│ └── visualizer.py
├── outputs/ # Saved charts and reports
├── images/ # Screenshots for documentation
├── app.py # Main Streamlit application
├── requirements.txt # Python dependencies
└── README.md

## 🚀 How to Run Locally

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/Expense-Tracker-App.git
   cd Expense-Tracker-App
  2 Create and activate virtual environment
   python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
3 Install dependencies
pip install -r requirements.txt
4Run the Streamlit app
streamlit run app.py
5 Open your browser at http://localhost:8501.
📊 Sample Outputs & Screenshots
Dashboard Overview
https://images/dashboard_overview.png

Monthly Spending Trend
https://images/monthly_trend.png

Payment Mode Analysis
https://images/payment_mode.png

Cumulative Spending
https://images/cumulative.png

More screenshots in the images/ folder.
🧪 Virtual Simulation
The app includes a synthetic data generator that mimics real-world expense patterns:

Higher food expenses on weekends.

Shopping spikes near month-end.

Bills concentrated in the first week.

Realistic category distributions (Food 25%, Shopping 18%, etc.).

This ensures you can fully demonstrate the app's capabilities without needing personal financial data.

📈 Key Insights Generated
"Your highest spending category is Food which accounts for 32.5% of total expenses."

"Spending increased by ₹2,450 compared to previous month."

"Most used payment method is UPI (45% of total)."

🤝 Contributing
Feel free to fork, open issues, or submit PRs. This project is intended for learning and portfolio building.

📄 License
MIT License – see LICENSE file.

👤 Author
* Hridoy Biswas *
GitHub : **https://github.com/erhridoybiswas**| LinkedIn : www.linkedin.com/in/erhridoybiswas



