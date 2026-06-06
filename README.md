# 📈 Stock Market Analysis Project

## Overview

This project is a comprehensive Stock Market Analysis solution built using Python, SQL, Power BI, and Streamlit. The objective is to collect, clean, analyze, visualize, and present stock market data from multiple NSE-listed companies through interactive dashboards and analytical reports.

The project combines data engineering, exploratory data analysis (EDA), business intelligence, and web-based visualization into a single end-to-end analytics workflow.

---

# 🎯 Project Objectives

* Analyze historical stock performance.
* Compare returns across multiple companies.
* Identify volatility patterns.
* Evaluate sector-wise performance.
* Visualize stock market trends.
* Build interactive dashboards using Power BI and Streamlit.
* Create a reusable analytics framework for future stock market research.

---

# 🛠️ Technologies Used

| Technology   | Purpose                         |
| ------------ | ------------------------------- |
| Python       | Data Collection & Analysis      |
| Pandas       | Data Cleaning & Manipulation    |
| NumPy        | Numerical Computation           |
| Matplotlib   | Visualization                   |
| Seaborn      | Advanced Visualization          |
| SQLite       | Data Storage                    |
| SQL          | Querying Data                   |
| Streamlit    | Interactive Dashboard           |
| Power BI     | Business Intelligence Dashboard |
| Git & GitHub | Version Control                 |

---

# 📂 Project Structure

```text
Stock_Analysis_Project/
│
├── csv_data/
├── data/
├── database/
│   ├── analysis_results/
│   ├── cleaning_summary.csv
│   └── stock_analysis.db
│
├── images/
│   ├── correlation_heatmap.png
│   ├── cumulative_return_chart.png
│   ├── sector_performance_chart.png
│   ├── streamlit_dashboard_overview.png
│   ├── streamlit_price_trend.png
│   └── volatility_chart.png
│
├── notebooks/
├── scripts/
├── streamlit_app/
│
├── powerbi/
│   ├── stock_market_dashboard.pbix
│   └── screenshots/
│       └── dashboard_powerbi.png
│
├── app.py
├── README.md
└── requirements.txt
```

---

# 📊 Power BI Dashboard

The Power BI dashboard provides an interactive view of stock market performance and key metrics.

### Features

* Total Stocks Tracked
* Average Closing Price
* Maximum Closing Price
* Total Trading Volume
* Stock Price Trend Analysis
* High vs Low Price Comparison
* Interactive Stock Selection
* Summary Analytics Table

### Dashboard Screenshot

![Power BI Dashboard](powerbi/screenshots/dashboard_powerbi.png)

---

# 🌐 Streamlit Dashboard

The Streamlit application enables users to interactively explore stock market data.

### Features

* Stock Selection
* Price Trend Analysis
* Volume Analysis
* Return Analysis
* Interactive Charts
* Real-Time Filtering

### Dashboard Preview

![Streamlit Dashboard](images/streamlit_dashboard_overview.png)

---

# 📈 Exploratory Data Analysis

## Sector Performance Analysis

This visualization compares average yearly returns across sectors.

![Sector Performance](images/sector_performance_chart.png)

---

## Stock Correlation Heatmap

The heatmap reveals relationships between stock movements and helps identify diversification opportunities.

![Correlation Heatmap](images/correlation_heatmap.png)

---

## Top Performing Stocks

Analysis of cumulative returns to identify the best-performing stocks.

![Cumulative Return](images/cumulative_return_chart.png)

---

## Volatility Analysis

Comparison of stock volatility to understand market risk and price fluctuations.

![Volatility Analysis](images/volatility_chart.png)

---

# 🗄️ Database

The project stores cleaned and processed data in SQLite.

Database file:

```text
database/stock_analysis.db
```

Benefits:

* Efficient querying
* Structured storage
* Easy integration with Power BI
* Faster analysis workflow

---

# 📋 Key Insights

* Several stocks demonstrated strong cumulative returns during the analysis period.
* Certain sectors significantly outperformed others.
* Trading volume spikes often coincided with major price movements.
* High correlation exists among some stocks, indicating sector influence.
* Volatility varies considerably across companies.

---

# 🚀 How to Run the Project

## Clone Repository

```bash
git clone <repository-url>
cd Stock_Analysis_Project
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Run Streamlit Dashboard

```bash
streamlit run streamlit_app/app.py
```

## Open Power BI Dashboard

Open:

```text
powerbi/stock_market_dashboard.pbix
```

using Power BI Desktop.

---

# 📌 Future Enhancements

* Real-time stock market integration
* Portfolio optimization module
* Machine Learning price prediction
* Risk-adjusted performance metrics
* Automated reporting
* Cloud deployment

---

# 👩‍💻 Author

Tania Banerjee

Data Analytics | Python | SQL | Power BI | Streamlit

This project demonstrates practical skills in data cleaning, analysis, visualization, dashboard development, and business intelligence.
