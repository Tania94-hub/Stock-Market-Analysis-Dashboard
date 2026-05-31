import os
import pandas as pd
import matplotlib.pyplot as plt

CSV_FOLDER = "csv_data"

# Load sector file
sector_df = pd.read_csv("Sector_data - Sheet1.csv")

# Extract ticker from Symbol column
sector_df["Ticker"] = (
    sector_df["Symbol"]
    .str.split(":")
    .str[-1]
    .str.strip()
)

sector_returns = []

for file in os.listdir(CSV_FOLDER):

    if not file.endswith(".csv"):
        continue

    ticker = file.replace(".csv", "")

    df = pd.read_csv(
        os.path.join(CSV_FOLDER, file)
    )

    # Sort by date
    df["Date"] = pd.to_datetime(df["Date"])
    df.sort_values("Date", inplace=True)

    # Calculate yearly return
    first_close = df.iloc[0]["Close"]
    last_close = df.iloc[-1]["Close"]

    yearly_return = (
        (last_close - first_close)
        / first_close
    ) * 100

    # Match ticker with sector
    sector_match = sector_df[
        sector_df["Ticker"] == ticker
    ]

    if len(sector_match) == 0:
        continue

    sector = sector_match.iloc[0]["sector"]

    sector_returns.append({
        "Ticker": ticker,
        "Sector": sector,
        "Return": yearly_return
    })

# Create DataFrame
sector_returns_df = pd.DataFrame(
    sector_returns
)

# Average return by sector
sector_performance = (
    sector_returns_df
    .groupby("Sector")["Return"]
    .mean()
    .reset_index()
)

sector_performance = (
    sector_performance
    .sort_values(
        "Return",
        ascending=False
    )
)

# Create output folder if needed
os.makedirs(
    "database/analysis_results",
    exist_ok=True
)

# Save CSV
sector_performance.to_csv(
    "database/analysis_results/sector_performance.csv",
    index=False
)

print("\nSector Performance\n")
print(sector_performance)

# Plot chart
plt.figure(figsize=(12, 6))

plt.bar(
    sector_performance["Sector"],
    sector_performance["Return"]
)

plt.title("Average Yearly Return by Sector")
plt.xlabel("Sector")
plt.ylabel("Average Return (%)")

plt.xticks(rotation=45)

plt.tight_layout()

# Save chart
plt.savefig(
    "database/analysis_results/sector_performance_chart.png"
)

plt.show()

print("\nSector Analysis Completed!")