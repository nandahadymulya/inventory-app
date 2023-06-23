from typing import Optional, List
from sqlmodel import Field, SQLModel, Relationship
from .roles import Roles

class UserBase(SQLModel):
    fullname: str = Field(index=True)
    username: str = Field(index=True)

    # role_id: Optional[int] = Field(default=None, foreign_key="roles.role_id")


class Users(UserBase, table=True):
    user_id: Optional[int] = Field(default=None, primary_key=True)

    # role: Optional[Roles] = Relationship(back_populates="users")


class UserRead(UserBase):
    fullname: str
    username: str


class UserCreate(UserBase):
    pass


class UserUpdate(SQLModel):
    fullname: Optional[str] = None
    username: Optional[str] = None
    password: Optional[str] = None
    role_id: Optional[int] = None
