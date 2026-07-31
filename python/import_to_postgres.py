import pandas as pd
from sqlalchemy import create_engine

# CSV file path
df = pd.read_csv(r"C:\Users\tannu\Downloads\customer_shopping_behavior.csv")

# PostgreSQL connection
engine = create_engine(
    "postgresql+psycopg2://postgres:1234@localhost:5432/customer_analysis"
)

# Import CSV into PostgreSQL
df.to_sql(
    "customer_shopping_behavior",
    engine,
    if_exists="replace",
    index=False
)

print("✅ Data imported successfully!")
