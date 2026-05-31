import os
import yaml
import pandas as pd
from collections import defaultdict

DATA_FOLDER = "data"
OUTPUT_FOLDER = "csv_data"

os.makedirs(OUTPUT_FOLDER, exist_ok=True)

stock_data = defaultdict(list)

for month_folder in os.listdir(DATA_FOLDER):

    month_path = os.path.join(DATA_FOLDER, month_folder)

    if not os.path.isdir(month_path):
        continue

    for yaml_file in os.listdir(month_path):

        if not yaml_file.endswith(".yaml"):
            continue

        file_path = os.path.join(month_path, yaml_file)

        with open(file_path, "r", encoding="utf-8") as file:
            data = yaml.safe_load(file)

        for record in data:

            ticker = record["Ticker"]

            stock_data[ticker].append({
                "Date": record["date"],
                "Open": record["open"],
                "High": record["high"],
                "Low": record["low"],
                "Close": record["close"],
                "Volume": record["volume"]
            })

for ticker, records in stock_data.items():

    df = pd.DataFrame(records)

    df["Date"] = pd.to_datetime(df["Date"])

    df.sort_values("Date", inplace=True)

    output_file = os.path.join(
        OUTPUT_FOLDER,
        f"{ticker}.csv"
    )

    df.to_csv(output_file, index=False)

print("All CSV files created successfully!")