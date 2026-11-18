from dotenv import find_dotenv,load_dotenv
import os 

_=load_dotenv(find_dotenv())


db_url=os.environ.get("DB_URL")
print(db_url)
