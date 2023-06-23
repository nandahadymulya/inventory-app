from typing import Optional, List
from sqlmodel import Field, SQLModel, Relationship
# from .roles import Roles

class ItemBase(SQLModel):
    name: str = Field(index=True)
    description: str = Field(index=True)
    quantity: int = Field(index=True)

    # role_id: Optional[int] = Field(default=None, foreign_key="roles.role_id")


class Items(ItemBase, table=True):
    item_id: Optional[int] = Field(default=None, primary_key=True)

    # role: Optional[Roles] = Relationship(back_populates="users")
