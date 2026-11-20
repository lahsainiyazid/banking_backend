from pydantic import BaseModel
from datetime import datetime 

class create_user(BaseModel):
    user_id:int 
    full_name:str
    email:str 
    created_at:datetime

class update_user(BaseModel):
    user_id:int|None=None 
    full_name:str|None=None
    email:str|None=None 
    created_at:datetime|None=None 
