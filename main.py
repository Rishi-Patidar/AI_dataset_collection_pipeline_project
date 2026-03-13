
import pandas as pd
import sqlite3

print("AI Dataset Pipeline")

df = pd.read_csv("data/ingested/metadata.csv")
print("Dataset rows:", len(df))

conn = sqlite3.connect("data/ingested/dataset.db")
sql = "SELECT label, COUNT(*) as count FROM dataset_metadata GROUP BY label"
print(pd.read_sql(sql,conn))
conn.close()

print("Pipeline completed successfully.")
