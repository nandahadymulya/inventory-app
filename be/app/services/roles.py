from fastapi import HTTPException, Query
from sqlmodel import Session, select
from ..models.roles import RoleRead, Roles


def create_role(session: Session, role: RoleRead):
    db_role = Roles(**role.dict())
    already_exists = session.exec(select(Roles).where(Roles.name == db_role.name)).first()
    if already_exists:
        raise HTTPException(status_code=400, detail="role already exists")
    session.add(db_role)
    session.commit()
    session.refresh(db_role)
    return db_role

def read_roles(
    session: Session,
    offset: int = 0,
    limit: int = Query(default=100, lte=100),
):
    roles = session.exec(select(Roles).offset(offset).limit(limit)).all()
    if roles == []:
        raise HTTPException(status_code=200, detail="roles is empty")
    return roles

def read_role_by_id(session: Session, role_id: int):
    db_role = session.get(Roles, role_id)
    if not db_role:
        raise HTTPException(status_code=404, detail="role not found")
    return db_role

def update_role(session: Session, role_id: int, role: RoleRead):
    db_role = session.get(Roles, role_id)
    if not db_role:
        raise HTTPException(status_code=404, detail="role not found")
    role_data = role.dict(exclude_unset=True)
    for key, value in role_data.items():
        setattr(db_role, key, value)
    session.add(db_role)
    session.commit()
    session.refresh(db_role)
    return db_role

def destroy_role(session: Session, role_id: int):
    role = session.get(Roles, role_id)
    if not role:
        raise HTTPException(status_code=404, detail="role not found")
    session.delete(role)
    session.commit()
    return {"messate": "role deleted successfully"}
