import sqlite3

conn = sqlite3.connect("sales.db")
cursor = conn.cursor()

print("Total Sales:")
cursor.execute("SELECT SUM(Sales) FROM sales_table;")
print(cursor.fetchone())

print("\nTotal Profit:")
cursor.execute("SELECT SUM(Profit) FROM sales_table;")
print(cursor.fetchone())

print("\nTop 5 Most Profitable Products:")
cursor.execute("""
SELECT Product_Name, Profit 
FROM sales_table 
ORDER BY Profit DESC 
LIMIT 5;
""")
print(cursor.fetchall())

print("\nSales by Region:")
cursor.execute("""
SELECT Region, SUM(Sales) 
FROM sales_table 
GROUP BY Region;
""")
print(cursor.fetchall())

conn.close()
