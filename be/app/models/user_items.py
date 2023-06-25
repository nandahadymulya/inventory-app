from typing import Optional
from sqlmodel import Field, SQLModel

class UserItemsBase(SQLModel):
    user_id: Optional[int] = Field(default=None)
    item_id: Optional[int] = Field(default=None)

class UserItems(UserItemsBase):
    user_items_id: Optional[int] = Field(default=None, primary_key=True)
