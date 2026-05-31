import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

CSV_FOLDER = "csv_data"

stock_prices = pd.DataFrame()

for file in os.listdir(CSV_FOLDER):

    if not file.endswith(".csv"):
        continue

    ticker = file.replace(".csv", "")

    df = pd.read_csv(
        os.path.join(CSV_FOLDER, file)
    )

    df["Date"] = pd.to_datetime(df["Date"])

    df = df[["Date", "Close"]]

    df.rename(
        columns={"Close": ticker},
        inplace=True
    )

    if stock_prices.empty:
        stock_prices = df
    else:
        stock_prices = pd.merge(
            stock_prices,
            df,
            on="Date",
            how="outer"
        )

stock_prices.sort_values(
    "Date",
    inplace=True
)

stock_prices.set_index(
    "Date",
    inplace=True
)

correlation_matrix = stock_prices.corr()

os.makedirs(
    "database/analysis_results",
    exist_ok=True
)

correlation_matrix.to_csv(
    "database/analysis_results/correlation_matrix.csv"
)

plt.figure(figsize=(18, 14))

sns.heatmap(
    correlation_matrix,
    cmap="coolwarm",
    center=0
)

plt.title("Stock Correlation Heatmap")

plt.tight_layout()

plt.savefig(
    "database/analysis_results/correlation_heatmap.png"
)

plt.show()

print("\nCorrelation Heatmap Created Successfully!")