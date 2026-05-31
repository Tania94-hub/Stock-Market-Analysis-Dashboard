import pandas as pd
import sqlite3
import os

# Database file
db_path = "database/stock_analysis.db"

# Connect to SQLite database
conn = sqlite3.connect(db_path)

csv_folder = "csv_data"

# Loop through all CSV files
for file in os.listdir(csv_folder):
    if file.endswith(".csv"):

        file_path = os.path.join(csv_folder, file)

        df = pd.read_csv(file_path)

        table_name = file.replace(".csv", "")

        df.to_sql(
            table_name,
            conn,
            if_exists="replace",
            index=False
        )

        print(f"{table_name} imported successfully")

conn.close()

print("\nDatabase Created Successfully!")