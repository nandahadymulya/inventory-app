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

def read_user_by_id(session: Session, user_id: int):
    user = session.get(Users, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="user not found")
    return user
