import psycopg 
from psycopg.rows import dict_row 
from db.db_url import db_url 
from routers.users.create_user import create_user


def get_all_accounts(url=db_url):
    with psycopg.connect(url,row_factory=dict_row) as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM accounts;")
            results=cur.fetchall()
            return results

def get_active_accounts(url=db_url):
    with psycopg.connect(url,row_factory=dict_row) as conn:
        with conn.cursor() as cur:
            cur.execute("""
            SELECT * FROM accounts 
            where status='active' ;
            """)
            results=cur.fetchall()
            return results

def get_non_active_accounts(url=db_url):
    with psycopg.connect(url,row_factory=dict_row) as conn:
        with conn.cursor() as cur:
            cur.execute("""
            SELECT * FROM accounts 
            where status<>'active' ;
            """)
            results=cur.fetchall()
            return results

def get_last_account_date(url=db_url):
    with psycopg.connect(url,row_factory=dict_row) as conn:
        with conn.cursor() as cur:
            cur.execute("""
            SELECT created_at FROM accounts
            order by created_at desc 
            limit 1;
                        """)
            result=cur.fetchone()
            return result

def get_accounts_by_balance(url=db_url):
    with psycopg.connect(url,row_factory=dict_row) as conn:
        with conn.cursor() as cur:
            cur.execute("""
            SELECT * FROM ACCOUNTS 
            order by balance desc;
                        """)
            results=cur.fetchall()
            return results


