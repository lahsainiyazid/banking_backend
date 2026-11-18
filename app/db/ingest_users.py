import os 
import psycopg 
import csv 
from db_url import db_url 
from datetime import datetime 
from decimal import Decimal 

user_query="""
 INSERT INTO users (user_id,full_name,email,created_at) values (%s,%s,%s,%s);
          """
def transform_row(row):
    return (
        int(row["user_id"]),
        row["full_name"],
        row["email"],
        datetime.fromisoformat(row["created_at"])
    )
def ingest_users(url=db_url):
    with psycopg.connect(url) as conn:
        with conn.cursor() as cur:
            with open("/home/yazid/banking/users.csv","r",encoding="utf-8") as f:
                reader=csv.DictReader(f)
                for row in reader:
                    clean_row=transform_row(row)
                    cur.execute(user_query,clean_row)

                

if __name__=="__main__":
    ingest_users()
