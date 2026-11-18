import psycopg 
from db.db_url import db_url 
from psycopg.rows import dict_row



def get_all_users(url=db_url):
    with psycopg.connect(url,row_factory=dict_row) as conn:
        with conn.cursor() as cur:
            cur.execute("""SELECT * from users;
                        """)
            results=cur.fetchall()
            return results
