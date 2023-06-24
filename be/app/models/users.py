from typing import Optional
from sqlmodel import Field, SQLModel


class UserBase(SQLModel):
    fullname: Optional[str] = Field(default="", index=True)
    username: str = Field(index=True)
    role_id: Optional[int] = Field(default=None, foreign_key="roles.role_id")

class Users(UserBase, table=True):
    user_id: Optional[int] = Field(default=None, primary_key=True)

class UserRead(UserBase):
    user_id: int
    role_id: int = Field(default=None, foreign_key="roles.role_id")

class UserCreate(UserBase):
    fullname: Optional[str] = ""
    username: str
    password: str
    role_id: Optional[int] = Field(default=None, foreign_key="roles.role_id")

class UserDelete(UserBase):
    fullname: Optional[str] = None
    password: Optional[str] = None
    role_id: Optional[int] = None

class UserUpdate(UserBase):
    fullname: Optional[str] = None
    password: Optional[str] = None
    role_id: Optional[int] = None
