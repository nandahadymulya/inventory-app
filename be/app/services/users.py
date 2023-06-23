from fastapi import HTTPException, Depends, Query
from sqlmodel import Session, select
from ..configs.database import get_engine
from ..models.users import Users

def get_session():
    engine = get_engine()
    with Session(engine) as session:
        yield session

def read_users(
    session: Session,
    offset: int = 0,
    limit: int = Query(default=100, lte=100),
):
    users = session.exec(select(Users).offset(offset).limit(limit)).all()
    return users


# def read_role_by_id(*, session: Session, role_id: int):
#     role = session.get(RolesRead, role_id)
#     if not role:
#         raise HTTPException(status_code=404, detail="role not found")
#     return role
