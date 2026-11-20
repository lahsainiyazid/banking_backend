import psycopg
from psycopg.rows import dict_row
import csv
from routers.db_url import db_url 


def get_all_users(url=db_url):
    with psycopg.connect(url,row_factory=dict_row) as conn:
        with conn.cursor() as cur:
            cur.exectue("SELECT * FROM users;")
            rows=cur.fetchall()
            return rows;

def get_latest_users(url=db_url):
    with psycopg.connect(url,row_factory=dict_row) as conn:
        with conn.curosr() as cur:
            cur.exectue("""SELECT * FROM user 
                order by created_at DESC; """)
            rows=cur.fetchall()
            return rows
