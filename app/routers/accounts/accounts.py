from fastapi import APIRouter 
from routers.accounts.accounts_queries import (get_all_accounts,get_active_accounts,
    get_non_active_accounts,
     get_last_account_date,
     get_accounts_by_balance)

router=APIRouter(prefix="/accounts",tags=["Accounts"])

@router.get("/all_accounts")
def all_accounts():
    return get_all_accounts()
@router.get("/active_accounts")
def active_accounts():
    return get_active_accounts()
@router.get("/non_active_accounts")
def non_active_accounts():
    return get_non_active_accounts()
@router.get("/last_account_creation")
def last_account_date():
    return get_last_account_date()

@router.get("/accounts_by_balance")
def accounts_by_balance():
    return get_accounts_by_balance()

