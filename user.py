from fastapi import APIRouter

router =APIRouter(
    prefix='/user',
    tags=['user'],
    responses={404 :{"description": "not found"}},

)

@router.get("/")
def read_user():
    return{"user":"User data"}

@router.get("/get")
def read_user():
    return{"user":"this is a new user data"}