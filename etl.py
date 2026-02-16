import pandas as pd
import sqlite3

print("Starting ETL process...")
# EXTRACT
print("Extracting data...")
df = df = pd.read_csv("sales.csv", encoding="latin1")
print("Data extracted successfully.")
print("Initial shape:", df.shape)

# TRANSFORM
print("Transforming data...")
df["Order Date"] = pd.to_datetime(df["Order Date"], errors="coerce")
df["Ship Date"] = pd.to_datetime(df["Ship Date"], errors="coerce")

numeric_columns = ["Sales", "Quantity", "Discount", "Profit"]
for col in numeric_columns:
    df[col] = pd.to_numeric(df[col], errors="coerce")

df = df.dropna()
df["Profit Margin"] = df["Profit"] / df["Sales"]
print("Transformation complete.")
print("Cleaned shape:", df.shape)
df.columns = df.columns.str.replace(" ", "_")

# LOAD
print("Loading data into SQLite database...")
conn = sqlite3.connect("sales.db")
df.to_sql("sales_table", conn, if_exists="replace", index=False)
conn.close()
print("Data loaded successfully into sales.db")
print("ETL process completed.")
