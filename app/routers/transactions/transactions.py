from fastapi import APIRouter
from routers.transactions.transactions_queries import (get_all_transactions
    ,get_top10_transactions,
    post_send_money,
    post_get_money)
from decimal import Decimal 

router=APIRouter(prefix="/transactions",tags=["Transactions"])
@router.get("/all_transactions")
def all_transactions():
    return get_all_transactions()

@router.get("/top10_transactions")
def top10_transactions():
    return get_top10_transactions()
@router.post("/send_money")
def send_money(send_id:int,receiver_id:int,amount:Decimal):
    return post_send_money(send_id,receiver_id,amount)
@router.post("/get_money")
def get_money(id:int,amount:Decimal):
    return post_get_money(id,amount)
