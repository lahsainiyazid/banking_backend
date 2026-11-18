import os 
import psycopg
import csv
from datetime import datetime
from decimal import Decimal 
from db_url import db_url 


account_query="""
 INSERT INTO accounts (account_id,user_id,account_type,currency,status,created_at,balance) 
 values (%s,%s,%s,%s,%s,%s,%s);
   """
def transform_row(row):
    return (
        int(row["account_id"]),
        int (row["user_id"]),
        row["account_type"],
        row["currency"],
        row["status"],
        datetime.fromisoformat(row["created_at"]),
        Decimal(row["balance"]))

def ingest_users(url=db_url):
    with psycopg.connect(url) as conn:
        with conn.cursor() as cur:
            with open("/home/yazid/banking/accounts.csv","r",encoding="utf-8") as f:
                rows=csv.DictReader(f)
                for row in rows:
                    cleaned_row=transform_row(row)
                    conn.execute(account_query,cleaned_row)


if __name__=="__main__":
    ingest_users()

