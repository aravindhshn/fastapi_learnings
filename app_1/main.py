from fastapi import FastAPI
from bcrypt import hashpw, gensalt, checkpw

from pydantic import BaseModel
# from uuid import UUID, uuid1
import uuid
import app_1.schema as schema
import logging


app = FastAPI()

valid_users = dict()
pending_users = dict()




@app.get('/cho1/index')
def index():
    return {"message": "Welcome To NARNIA"}



@app.get('/login')
def login(username: str, password: str):
    """
    Api for login
    """
    if not valid_users.get(username):
        return {'message': 'invalid user'}
    else:
        users = valid_users.get(username)
        password = valid_users.get(password)
        if users and password:
            return {"msg": "Valid User"}


@app.post('/login/signup')
def signup(uname: str, password: str):
    """
    API TO SIGNUP FOR  THE NEW USERS
    """
    if not uname or not password:
        return {'message': "provide valid details"}
    elif valid_users.get(uname):
        logging.info(type(valid_users))
        return {'message': 'user exists'}
    else:
        print("helllo", pending_users)
        logging.info(type(valid_users))
        user = schema.User(username=uname, password=password)
        logging.info(user.username)
        pending_users[uname] = user
        return {"user": user.username}



@app.get('/get/pending_users')
def get_pending_user():
    return pending_users





@app.post('/validation/user', response_model=schema.ValidUser)
def validata_user(user: schema.User):
    if valid_users.get(user.username):
        return valid_users[user.username]
    elif user.username in pending_users:
        valid_user = schema.ValidUser(username=user.username, password = user.password, passphrase=hashpw(user.password.encode(), gensalt()), id=uuid.uuid4().hex)
        valid_users[user.username] = dict(valid_user)
        pending_users.pop(user.username, None)
        return valid_user


@app.get('/valid_users')
def get_valid_users():
    return valid_users



@app.put("/update/user/details/{username}")
def update_user_details(username: str,user_details: schema.UserDetails, response_model = schema.UserProfile):
    age = user_details.age
    place = user_details.place
    print(place, age)

    if valid_users.get(username):
        print('valid users', valid_users, username, type(username))
        valid_users[username]['age'] = age
        valid_users[username]['place'] = place
        return valid_users[username]
    else:
        return {'msg': 'user_details is not present'}
