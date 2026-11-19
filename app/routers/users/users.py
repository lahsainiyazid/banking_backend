from fastapi import APIRouter
from routers.users.users_queries import (get_all_users,get_latest_users,get_user_by_id,
post_user)
from routers.users.create_user import create_user
router=APIRouter(prefix="/users",tags=["Users"])

@router.get("/get_users")
def all_users():
    return get_all_users()

@router.get("/latest_users")
def latest_users():
    return get_latest_users()
@router.get("/user_by_id")
def user_by_id(id:int):
    return get_user_by_id(id)

@router.post("/add_user")
def add_user(user:create_user):
    return post_user(user)
