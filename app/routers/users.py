from fastapi import APIRouter
from routers.users_queries import (get_all_users,get_latest_users)


router=APIRouter(prefix="/users",tags=["Users"])

@router.get("/get_users")
def all_users():
    return get_all_users()

@router.get("/latest_users")
def latest_users():
    return get_latest_users()
