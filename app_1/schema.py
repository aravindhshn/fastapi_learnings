from pydantic import BaseModel
from uuid import UUID



class ValidUser(BaseModel):
    # id: UUID
    username: str
    password: str
    passphrase: str

   
class User(BaseModel):
    username: str
    password: str


class ValidUser(BaseModel):
    username: str
    password: str
    passphrase: str
    id: UUID

class User(BaseModel):
    username: str
    password: str



class UserProfile(BaseModel):
    username: str
    age: int
    place: str


class UserDetails(BaseModel):
    age: int
    place: str