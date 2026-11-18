import psycopg 
from psycopg.rows import dict_row 
from routers.db_url import db_url 

def get_all_transactions(url=db_url):
    with psycopg.connect(url,row_factory=dict_row) as conn :
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM TRANSACTIONS;")
            rows=cur.fetchall()
            return rows

def get_top10_transactions(url=db_url):
    with psycopg.connect(url,row_factory=dict_row) as conn:
        with conn.cursor() as cur:
            cur.execute("""SELECT * FROM TRANSACTIONS 
            order by amount desc 
            limit 10;""")
            results=cur.fetchall()
            return results
