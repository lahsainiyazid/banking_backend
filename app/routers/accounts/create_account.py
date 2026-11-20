from pydantic import BaseModel,Field
from typing import Literal
from datetime import datetime 
from decimal import Decimal 

class create_account(BaseModel):
    account_id:int
    user_id:int 
    account_type:Literal["checking","savings"]
    currency:Literal ["MAD"]=Field(description="Currency,Only MAD is supported")
    status:Literal["active","frozen","closed"]=Field(default="active",
    description="Three valid values active,frozen,closed default is active")
    created_at:datetime=Field(description="Date of creation of the account")
    balance:Decimal=Field(default=Decimal("0.00"),ge=0)
class update_status(BaseModel):
    status:Literal["active","frozen","closed"]
