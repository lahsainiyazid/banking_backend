from fastapi import APIRouter
from routers.transactions.transactions_queries import (get_all_transactions,get_top10_transactions)


router=APIRouter(prefix="/transactions",tags=["Transactions"])
@router.get("/all_transactions")
def all_transactions():
    return get_all_transactions()

@router.get("/top10_transactions")
def top10_transactions():
    return get_top10_transactions()
