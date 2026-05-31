import os
import pandas as pd

CSV_FOLDER = "csv_data"

monthly_results = []

for file in os.listdir(CSV_FOLDER):

    if not file.endswith(".csv"):
        continue

    ticker = file.replace(".csv", "")

    df = pd.read_csv(
        os.path.join(CSV_FOLDER, file)
    )

    df["Date"] = pd.to_datetime(df["Date"])

    df["Month"] = (
        df["Date"]
        .dt.to_period("M")
        .astype(str)
    )

    monthly_return = (
        df.groupby("Month")
        .apply(
            lambda x:
            ((x.iloc[-1]["Close"] -
              x.iloc[0]["Close"])
             / x.iloc[0]["Close"]) * 100
        )
        .reset_index()
    )

    monthly_return.columns = [
        "Month",
        "Return"
    ]

    monthly_return["Ticker"] = ticker

    monthly_results.append(
        monthly_return
    )

monthly_df = pd.concat(
    monthly_results,
    ignore_index=True
)

top_gainers = (
    monthly_df
    .sort_values(
        "Return",
        ascending=False
    )
    .groupby("Month")
    .head(5)
)

top_losers = (
    monthly_df
    .sort_values(
        "Return",
        ascending=True
    )
    .groupby("Month")
    .head(5)
)

top_gainers.to_csv(
    "database/analysis_results/monthly_top_gainers.csv",
    index=False
)

top_losers.to_csv(
    "database/analysis_results/monthly_top_losers.csv",
    index=False
)

print("\nTop Monthly Gainers\n")
print(top_gainers.head(20))

print("\nTop Monthly Losers\n")
print(top_losers.head(20))

print(
    "\nMonthly Gainers & Losers Analysis Completed!"
)