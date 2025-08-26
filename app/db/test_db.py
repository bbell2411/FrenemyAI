import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

print(f"Trying to connect to: {DATABASE_URL}")

try:
    conn = psycopg2.connect(DATABASE_URL)
    print("✅ SUCCESS! Connected to database!")
    conn.close()
except Exception as e:
    print(f"❌ FAILED: {e}")