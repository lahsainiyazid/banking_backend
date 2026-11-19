from pydantic import BaseModel 
from datetime import datetime

class update_user(BaseModel):
    user_id:int|None 
    full_name:str|None 
    email:str|None
    created_at:datetime|None 
