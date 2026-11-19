import psycopg 
from db.db_url import db_url 
from psycopg.rows import dict_row
from routers.users.create_user import create_user


def get_all_users(url=db_url):
    with psycopg.connect(url,row_factory=dict_row) as conn:
        with conn.cursor() as cur:
            cur.execute("""SELECT * from users;
                        """)
            results=cur.fetchall()
            return results

def get_latest_users(url=db_url):
    with psycopg.connect(url,row_factory=dict_row) as conn:
        with conn.cursor() as cur:
            cur.execute("""SELECT user_id,full_name from users 
                order by created_at desc 
                 LIMIT 3;""")
            results=cur.fetchall()
            return results
def get_user_by_id(id:int,url=db_url):
    with psycopg.connect(url,row_factory=dict_row) as conn:
        with conn.cursor() as cur:
            cur.execute("""
            SELECT * FROM users 
            where user_id=%s; 
                        """,(id,))
            result=cur.fetchone()
            return result

def post_user(user:create_user,url=db_url):
    with psycopg.connect(url,row_factory=dict_row) as conn:
        with conn.cursor() as cur:
            cur.execute("""
            INSERT INTO USERS (user_id,full_name,created_at,email) VALUES(%s,%s,%s,%s)
                       ;""",(user.user_id,user.full_name,user.created_at,user.email))
