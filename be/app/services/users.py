from fastapi import HTTPException, Query
from sqlmodel import Session, select
from ..models.users import Users, UserRead
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def create_user(session: Session, user: UserRead):
    db_user = Users(**user.dict())
    already_exists = session.exec(select(Users).where(Users.username == db_user.username)).first()
    if already_exists:
        raise HTTPException(status_code=400, detail="user already exists")
    db_user.password = pwd_context.hash(db_user.password)

    session.add(db_user)
    session.commit()
    session.refresh(db_user)
    return db_user

def read_users(
    session: Session,
    offset: int = 0,
    limit: int = Query(default=100, lte=100),
):
    users = session.exec(select(Users).offset(offset).limit(limit)).all()
    if users == []:
        raise HTTPException(status_code=200, detail="users is empty")
    return users

def read_user_by_id(session: Session, user_id: int):
    user = session.get(Users, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="user not found")
    return user

def update_user(session: Session, user_id: int, user: UserRead):
    db_user = session.get(Users, user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="user not found")
    user_data = user.dict(exclude_unset=True)
    for key, value in user_data.items():
        setattr(db_user, key, value)
    session.add(db_user)
    session.commit()
    session.refresh(db_user)
    return db_user

def destroy_user(session: Session, user_id: int):
    user = session.get(Users, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="user not found")
    session.delete(user)
    session.commit()
    return {"messate": "user deleted successfully"}
