import os
import pandas as pd
import matplotlib.pyplot as plt

CSV_FOLDER = "csv_data"

performance_data = []

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

    performance_data.append({
        "Ticker": file.replace(".csv", ""),
        "Return": yearly_return
    })

performance_df = pd.DataFrame(performance_data)

top_5 = (
    performance_df
    .sort_values("Return", ascending=False)
    .head(5)
)

plt.figure(figsize=(12, 6))

for ticker in top_5["Ticker"]:

    df = pd.read_csv(
        os.path.join(
            CSV_FOLDER,
            f"{ticker}.csv"
        )
    )

    df["Date"] = pd.to_datetime(df["Date"])
    df.sort_values("Date", inplace=True)

    df["Daily_Return"] = df["Close"].pct_change()

    df["Cumulative_Return"] = (
        1 + df["Daily_Return"]
    ).cumprod() - 1

    plt.plot(
        df["Date"],
        df["Cumulative_Return"],
        label=ticker
    )

plt.title("Top 5 Performing Stocks - Cumulative Return")
plt.xlabel("Date")
plt.ylabel("Cumulative Return")
plt.legend()

plt.tight_layout()

os.makedirs(
    "database/analysis_results",
    exist_ok=True
)

plt.savefig(
    "database/analysis_results/cumulative_return_chart.png"
)

top_5.to_csv(
    "database/analysis_results/top_5_performing_stocks.csv",
    index=False
)

plt.show()

print("\nTop 5 Performing Stocks\n")
print(top_5)

print("\nCumulative Return Analysis Completed!")