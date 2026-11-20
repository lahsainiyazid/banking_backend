import psycopg 
from psycopg.rows import dict_row 
from uuid import uuid4
from datetime import datetime 
from decimal import Decimal 
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

def post_send_money(sender_id:int,receiver_id:int,amount:Decimal,url=db_url):
    if (amount<=0 or sender_id==receiver_id):
        raise ValueError("Invalid Transaction!")
    with psycopg.connect(url) as conn:
        with conn.cursor() as cur:
            cur.execute("""
            UPDATE accounts set balance=balance-%s
            where 
            account_id=%s and status='active'
            and balance>=%s; 
                        """,(amount,sender_id,amount))
            if cur.rowcount!=1:
                raise ValueError("Invalid Transaction!")
            cur.execute("""
            UPDATE accounts set balance=balance+%s
            where 
            account_id=%s and status='active';
                        """,(amount,receiver_id))
            if cur.rowcount!=1:
                raise ValueError("Invalid Transaction!")
            reference=str(uuid4())
            cur.execute("""
            INSERT INTO transactions (destination_account_id,amount,created_at,reference)
            VALUES (%s,%s,%s,%s);
                        """,(receiver_id,amount,datetime.now(),reference))
