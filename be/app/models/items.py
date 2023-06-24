from typing import Optional
from sqlmodel import Field, SQLModel


class ItemBase(SQLModel):
    name: str = Field(index=True)
    description: Optional[str] = Field(default="",index=True)
    quantity: int = Field(index=True)

class Items(ItemBase, table=True):
    item_id: Optional[int] = Field(default=None, primary_key=True)

class ItemRead(ItemBase):
    item_id: int

class ItemCreate(ItemBase):
    item_id: Optional[int] = Field(default=None, primary_key=True)
    name: Optional[str] = ""
    description: str
    quantity: int
