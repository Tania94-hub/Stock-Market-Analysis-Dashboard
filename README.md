# 📈 Stock Market Analysis Dashboard

A complete Stock Market Analysis project built using **Python**, **SQLite**, **Streamlit**, and **Power BI**. This project collects stock data, performs data cleaning and analysis, stores processed data in a database, generates visualizations, and provides interactive dashboards for business insights.

---

## 🚀 Project Overview

This project analyzes stock market performance using multiple analytical techniques:

- Data Collection from CSV files
- Data Cleaning and Transformation
- SQLite Database Integration
- Correlation Analysis
- Cumulative Return Analysis
- Sector Performance Analysis
- Monthly Gainers and Losers Analysis
- Volatility Analysis
- Interactive Streamlit Dashboard
- Power BI Dashboard Reporting

The objective is to provide meaningful insights into stock behavior, sector trends, risk levels, and overall market performance.

---

## 🛠️ Technologies Used

| Technology | Purpose |
|------------|----------|
| Python | Data Processing & Analysis |
| Pandas | Data Manipulation |
| NumPy | Numerical Computation |
| Matplotlib | Visualization |
| Seaborn | Heatmap Generation |
| SQLite | Database Storage |
| Streamlit | Interactive Dashboard |
| Power BI | Business Intelligence Dashboard |

---

## 📂 Project Structure

```text
Stock_Market_Analysis_Project/
│
├── csv_data/
│
├── database/
│   ├── analysis_results/
│   ├── cleaning_summary.csv
│   └── stock_analysis.db
│
├── images/
│   ├── correlation_heatmap.png
│   ├── cumulative_return_chart.png
│   ├── market_summary_dashboard.png
│   ├── sector_performance_chart.png
│   ├── streamlit_dashboard.png
│   └── volatility_chart.png
│
├── notebooks/
│
├── powerbi/
│   └── Stock_Market_Analysis.pbix
│
├── scripts/
│   ├── yaml_to_csv.py
│   ├── data_cleaning.py
│   ├── analysis.py
│   ├── volatility_analysis.py
│   ├── cumulative_return.py
│   ├── sector_analysis.py
│   ├── correlation_heatmap.py
│   ├── monthly_gainers_losers.py
│   └── database_setup.py
│
├── streamlit_app/
│   └── app.py
│
├── README.md
└── requirements.txt
```

---

## 📊 Power BI Dashboard

The project includes a Power BI dashboard that provides:

- Market Summary
- Monthly Gainers
- Monthly Losers
- Sector Performance
- Top Performing Stocks
- Most Volatile Stocks
- Return Analysis

### Market Summary Dashboard

![Market Summary Dashboard](images/market_summary_dashboard.png)

---

## 🌐 Streamlit Dashboard

Interactive dashboard built with Streamlit for real-time exploration of stock market insights.

![Streamlit Dashboard](images/streamlit_dashboard.png)

---

# 📈 Analysis Visualizations

## 🔥 Correlation Heatmap

Displays correlation between stocks and identifies highly related securities.

![Correlation Heatmap](images/correlation_heatmap.png)

---

## 📊 Cumulative Return Analysis

Tracks cumulative returns across selected stocks over time.

![Cumulative Return Analysis](images/cumulative_return_chart.png)

---

## 🏭 Sector Performance Analysis

Compares stock returns across different market sectors.

![Sector Performance Analysis](images/sector_performance_chart.png)

---

## 📉 Volatility Analysis

Identifies the most volatile stocks based on historical performance.

![Volatility Analysis](images/volatility_chart.png)

---

## ⚙️ Features

✅ Data Cleaning and Validation

✅ SQLite Database Storage

✅ Automated Analysis Scripts

✅ Correlation Matrix Generation

✅ Volatility Analysis

✅ Sector-wise Performance Tracking

✅ Monthly Top Gainers and Losers

✅ Power BI Dashboard

✅ Streamlit Interactive Dashboard

---

## ▶️ How To Run

### 1. Clone Repository

```bash
git clone https://github.com/Tania94-hub/Stock-Market-Analysis-Dashboard.git
```

### 2. Move into Project Directory

```bash
cd Stock-Market-Analysis-Dashboard
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run Data Cleaning

```bash
python scripts/data_cleaning.py
```

### 5. Setup Database

```bash
python scripts/database_setup.py
```

### 6. Run Analysis Scripts

```bash
python scripts/analysis.py
python scripts/correlation_heatmap.py
python scripts/cumulative_return.py
python scripts/sector_analysis.py
python scripts/volatility_analysis.py
python scripts/monthly_gainers_losers.py
```

### 7. Launch Streamlit Dashboard

```bash
streamlit run streamlit_app/app.py
```

---

## 📌 Key Insights Generated

- Most Volatile Stocks
- Best Performing Stocks
- Worst Performing Stocks
- Sector-wise Returns
- Stock Correlation Patterns
- Monthly Top Gainers
- Monthly Top Losers
- Long-term Return Trends

---

## 📄 License

This project is licensed under the MIT License.

---

## 👩‍💻 Author

**Tania Banerjee**

GitHub: https://github.com/Tania94-hub

---

⭐ If you found this project useful, consider giving it a star.
