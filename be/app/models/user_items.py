from typing import Optional, List
from sqlmodel import Field, SQLModel, Relationship
# from .roles import Roles

class ItemBase(SQLModel):
    fullname: str = Field(index=True)
    quantity: int = Field(index=True)


class Items(ItemBase, table=True):
    user_items_id: Optional[int] = Field(default=None, primary_key=True)
    user_id: Optional[int] = Field(default=None)
    item_id: Optional[int] = Field(default=None)
