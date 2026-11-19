from pydantic import BaseModel
from datetime import datetime 

class create_user(BaseModel):
    user_id:int 
    full_name:str
    email:str 
    created_at:datetime
