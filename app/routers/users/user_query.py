import psycopg
from psycopg.rows import dict_row
import csv
from routers.db_url import db_url 
from routers.users.user_classes import create_user

def get_all_users(url=db_url):
    with psycopg.connect(url,row_factory=dict_row) as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM users;")
            rows=cur.fetchall()
            return rows;

def get_latest_users(url=db_url):
    with psycopg.connect(url,row_factory=dict_row) as conn:
        with conn.cursor() as cur:
            cur.execute("""SELECT * FROM users 
                order by created_at DESC; """)
            rows=cur.fetchall()
            return rows

def get_user_by_id(id:int,url=db_url):
    with psycopg.connect(url) as conn:
        with conn.cursor() as cur:
            cur.exectue("""SELECT * FROM users
                where user_id=%s;""",(id,))

def post_user(new_user:create_user):
    with psycopg.connect(url) as conn:
        with conn.cursor() as cur:
            cur.execute("""INSERT INTO users (user_id,full_name,email,created_at)
            values (%s,%s,%s,%s);""",
        (new_user.user_id,new_user.full_name,new_user.email,new_user.created_at))
