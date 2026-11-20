from pydantic import BaseModel,Field



class widthrawal(BaseModel):
    amount:int=Field(gt=0)
    sender_account:int=Field(gt=-1)
    receiver_account:int=Field(gt=-1)
    sent:bool 
    received:bool 
