from typing import Optional
from sqlmodel import Field, SQLModel


class RolesBase(SQLModel):
    name: str = Field(unique=True, index=True)

class Roles(RolesBase, table=True):
    role_id: Optional[int] = Field(default=None, primary_key=True)

class RolesRead(RolesBase):
    role_id: int
