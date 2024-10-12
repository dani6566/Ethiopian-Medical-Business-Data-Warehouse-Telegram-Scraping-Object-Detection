import os
import psycopg2
import pandas as pd
import csv
from dotenv import load_dotenv



# Load environment variables from .env file
load_dotenv()

# Fetch database connection parameters from environment variables
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

# Establish a connection to the database
conn = psycopg2.connect(
    host=DB_HOST,
    port=DB_PORT,
    database=DB_NAME,
    user=DB_USER,
    password=DB_PASSWORD
)

# Create a cursor object
cur = conn.cursor()

# Open the CSV file
with open('../data/cleaned_data.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    next(reader)  # Skip the header row

    for row in reader:
        cur.execute(
            "INSERT INTO data_warehouse (channel_title, channel_username, id, message, date, media_path) VALUES (%s, %s, %s, %s, %s, %s)",
            row
        )

# Commit the transaction
conn.commit()

# Close the cursor and connection
cur.close()
conn.close()