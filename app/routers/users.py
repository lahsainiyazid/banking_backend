from fastapi import APIRouter
from routers.users_queries import (get_all_users)


router=APIRouter(prefix="/users",tags=["Users"])

@router.get("/get_users")
def all_users():
    return get_all_users()
