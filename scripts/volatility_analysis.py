import os
import pandas as pd
import matplotlib.pyplot as plt

CSV_FOLDER = "csv_data"

volatility_data = []

for file in os.listdir(CSV_FOLDER):

    if not file.endswith(".csv"):
        continue

    file_path = os.path.join(CSV_FOLDER, file)

    df = pd.read_csv(file_path)

    df["Daily_Return"] = df["Close"].pct_change()

    volatility = df["Daily_Return"].std()

    volatility_data.append({
        "Ticker": file.replace(".csv", ""),
        "Volatility": volatility
    })

volatility_df = pd.DataFrame(volatility_data)

top_10_volatile = (
    volatility_df
    .sort_values("Volatility", ascending=False)
    .head(10)
)

# Save results
os.makedirs(
    "database/analysis_results",
    exist_ok=True
)

top_10_volatile.to_csv(
    "database/analysis_results/top_10_volatile_stocks.csv",
    index=False
)

print("\nTop 10 Most Volatile Stocks\n")
print(top_10_volatile)

# Plot
plt.figure(figsize=(10, 6))

plt.bar(
    top_10_volatile["Ticker"],
    top_10_volatile["Volatility"]
)

plt.title("Top 10 Most Volatile Stocks")
plt.xlabel("Stock")
plt.ylabel("Volatility")

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig(
    "database/analysis_results/volatility_chart.png"
)

plt.show()

print("\nVolatility Analysis Completed!")