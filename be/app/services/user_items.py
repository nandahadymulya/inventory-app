from fastapi import HTTPException, Depends, Query
from sqlmodel import Session, select
from ..configs.database import get_engine
# from ..models.items_user import ItemsUser

def get_session():
    engine = get_engine()
    with Session(engine) as session:
        yield session

def read_items(session: Session):
    items = session.exec(select(Items)).all()
    print(items)
    return items
