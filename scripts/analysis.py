import os
import pandas as pd

CSV_FOLDER = "csv_data"

results = []

all_prices = []
all_volumes = []

for file in os.listdir(CSV_FOLDER):

    if not file.endswith(".csv"):
        continue

    file_path = os.path.join(CSV_FOLDER, file)

    df = pd.read_csv(file_path)

    df["Date"] = pd.to_datetime(df["Date"])
    df.sort_values("Date", inplace=True)

    first_close = df.iloc[0]["Close"]
    last_close = df.iloc[-1]["Close"]

    yearly_return = (
        (last_close - first_close)
        / first_close
    ) * 100

    results.append({
        "Ticker": file.replace(".csv", ""),
        "Yearly_Return (%)": round(yearly_return, 2)
    })

    all_prices.extend(df["Close"].tolist())
    all_volumes.extend(df["Volume"].tolist())

returns_df = pd.DataFrame(results)

# Top 10 Green Stocks
top_green = returns_df.sort_values(
    "Yearly_Return (%)",
    ascending=False
).head(10)

# Top 10 Loss Stocks
top_loss = returns_df.sort_values(
    "Yearly_Return (%)"
).head(10)

# Market Summary
green_count = (returns_df["Yearly_Return (%)"] > 0).sum()
red_count = (returns_df["Yearly_Return (%)"] < 0).sum()

avg_price = round(sum(all_prices) / len(all_prices), 2)
avg_volume = round(sum(all_volumes) / len(all_volumes), 2)

market_summary = pd.DataFrame({
    "Metric": [
        "Green Stocks",
        "Red Stocks",
        "Average Price",
        "Average Volume"
    ],
    "Value": [
        green_count,
        red_count,
        avg_price,
        avg_volume
    ]
})

# Create output folder
os.makedirs("database/analysis_results",
            exist_ok=True)

top_green.to_csv(
    "database/analysis_results/top_10_green_stocks.csv",
    index=False
)

top_loss.to_csv(
    "database/analysis_results/top_10_loss_stocks.csv",
    index=False
)

market_summary.to_csv(
    "database/analysis_results/market_summary.csv",
    index=False
)

print("\nTop 10 Green Stocks\n")
print(top_green)

print("\nTop 10 Loss Stocks\n")
print(top_loss)

print("\nMarket Summary\n")
print(market_summary)

print("\nAnalysis Completed Successfully!")