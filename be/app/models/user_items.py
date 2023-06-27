from typing import Optional
from sqlmodel import Field, SQLModel


class UserItemsBase(SQLModel):
    user_id: Optional[int] = Field(default=0)
    item_id: Optional[int] = Field(default=0)
    amount: Optional[int] = Field(default=0)

class UserItems(UserItemsBase):
    user_items_id: Optional[int] = Field(default=None, primary_key=True)
