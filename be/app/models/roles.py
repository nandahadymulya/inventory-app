from typing import Optional, List
from sqlmodel import Field, SQLModel, Relationship

class SensitiveRole(SQLModel):
    role_id: int
    name: str

class RolesBase(SQLModel):
    name: str = Field(unique=True, index=True)

class Roles(RolesBase, table=True):
    role_id: Optional[int] = Field(default=None, primary_key=True)

    # users: List["Users"] = Relationship(back_populates="roles")

    # def to_sensitive_role(self) -> SensitiveRole:
        # return SensitiveRole(role_id=self.role_id, name=self.name),

class RolesRead(RolesBase):
    name: str

# class RolesCreate(Roles):
#     pass

# class RolesUpdate(Roles):
#     pass

# class RolesDelete(Roles):
#     pass

from .users import Users
