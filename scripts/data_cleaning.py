import os
import pandas as pd

CSV_FOLDER = "csv_data"

summary = []

for file in os.listdir(CSV_FOLDER):

    if not file.endswith(".csv"):
        continue

    file_path = os.path.join(CSV_FOLDER, file)

    df = pd.read_csv(file_path)

    # Convert date
    df["Date"] = pd.to_datetime(df["Date"])

    # Remove duplicates
    duplicates = df.duplicated().sum()
    df.drop_duplicates(inplace=True)

    # Missing values
    missing_values = df.isnull().sum().sum()

    # Sort by date
    df.sort_values("Date", inplace=True)

    # Save cleaned file
    df.to_csv(file_path, index=False)

    summary.append({
        "Stock": file,
        "Rows": len(df),
        "Duplicates Removed": duplicates,
        "Missing Values": missing_values
    })

summary_df = pd.DataFrame(summary)

print("\nData Cleaning Summary\n")
print(summary_df)

summary_df.to_csv(
    "database/cleaning_summary.csv",
    index=False
)

print("\nCleaning Completed Successfully!")