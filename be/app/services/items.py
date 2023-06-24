from fastapi import HTTPException, Depends, Query
from sqlmodel import Session, select
from ..configs.database import get_engine
from ..models.items import Items

def get_session():
    engine = get_engine()
    with Session(engine) as session:
        yield session

def read_items(session: Session):
    items = session.exec(select(Items)).all()
    print(items)
    return items

def read_item_by_id(session: Session, item_id: int):
    item = session.get(Items, item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

def create_item(*, session: Session, item: Items):
    print(item)
    print(session)
    # session.add(items)
    # session.commit()
    # session.refresh(items)
    # return item
