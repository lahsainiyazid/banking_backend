import os 
import csv 
import psycopg
from datetime import datetime 
from decimal import Decimal 
from db_url import db_url 

transaction_query="""
    insert into transactions 
    (transaction_type,source_account_id,destination_account_id,amount,created_at,reference)
    values (%s,%s,%s,%s,%s,%s)
    """

def transform_row(row):
    return (
        row["transaction_type"],
        int (row["source_account_id"]) if row["source_account_id"] else None,
        int (row["destination_account_id"]) if row["destination_account_id"] else None ,
        Decimal(row["amount"]),
        datetime.fromisoformat(row["created_at"]),
        row["reference"]
    )

def ingest_transactions(url=db_url):
    with psycopg.connect(url) as conn:
        with conn.cursor() as cur:
            with open("/home/yazid/banking/transactions.csv","r",encoding="utf-8") as f:
                rows=csv.DictReader(f)
                for row in rows:
                    clean_row=transform_row(row)
                    cur.execute(transaction_query,clean_row)

if __name__=="__main__":
    ingest_transactions()
