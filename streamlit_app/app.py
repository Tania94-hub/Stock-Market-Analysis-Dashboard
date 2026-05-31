import streamlit as st
import pandas as pd
from PIL import Image

# =====================================
# Page Configuration
# =====================================

st.set_page_config(
    page_title="Stock Market Analysis Dashboard",
    layout="wide"
)

st.title("📈 Stock Market Analysis Dashboard")
st.markdown("---")

# =====================================
# Market Summary
# =====================================

st.header("📊 Market Summary")

market_summary = pd.read_csv(
    "database/analysis_results/market_summary.csv"
)

st.dataframe(
    market_summary,
    use_container_width=True
)

# =====================================
# Top Green Stocks
# =====================================

st.header("🟢 Top 10 Green Stocks")

green_stocks = pd.read_csv(
    "database/analysis_results/top_10_green_stocks.csv"
)

st.dataframe(
    green_stocks,
    use_container_width=True
)

# =====================================
# Top Loss Stocks
# =====================================

st.header("🔴 Top 10 Loss Stocks")

loss_stocks = pd.read_csv(
    "database/analysis_results/top_10_loss_stocks.csv"
)

st.dataframe(
    loss_stocks,
    use_container_width=True
)

# =====================================
# Top Volatile Stocks
# =====================================

st.header("⚡ Top 10 Volatile Stocks")

volatile_stocks = pd.read_csv(
    "database/analysis_results/top_10_volatile_stocks.csv"
)

st.dataframe(
    volatile_stocks,
    use_container_width=True
)

# =====================================
# Sector Performance
# =====================================

st.header("🏭 Sector Performance")

sector_df = pd.read_csv(
    "database/analysis_results/sector_performance.csv"
)

st.dataframe(
    sector_df,
    use_container_width=True
)

sector_chart = Image.open(
    "database/analysis_results/sector_performance_chart.png"
)

st.image(
    sector_chart,
    caption="Average Yearly Return by Sector",
    use_container_width=True
)

# =====================================
# Volatility Chart
# =====================================

st.header("📈 Volatility Analysis")

volatility_chart = Image.open(
    "database/analysis_results/volatility_chart.png"
)

st.image(
    volatility_chart,
    caption="Top 10 Most Volatile Stocks",
    use_container_width=True
)

# =====================================
# Correlation Heatmap
# =====================================

st.header("🔥 Correlation Heatmap")

heatmap_chart = Image.open(
    "database/analysis_results/correlation_heatmap.png"
)

st.image(
    heatmap_chart,
    caption="Stock Correlation Heatmap",
    use_container_width=True
)

# =====================================
# Monthly Top Gainers
# =====================================

st.header("🚀 Monthly Top Gainers")

monthly_gainers = pd.read_csv(
    "database/analysis_results/monthly_top_gainers.csv"
)

st.dataframe(
    monthly_gainers,
    use_container_width=True
)

# =====================================
# Monthly Top Losers
# =====================================

st.header("📉 Monthly Top Losers")

monthly_losers = pd.read_csv(
    "database/analysis_results/monthly_top_losers.csv"
)

st.dataframe(
    monthly_losers,
    use_container_width=True
)

# =====================================
# Footer
# =====================================

st.markdown("---")

st.success(
    "Stock Market Analysis Dashboard Loaded Successfully!"
)