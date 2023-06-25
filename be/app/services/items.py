from fastapi import status, Query
from sqlmodel import Session, select
from fastapi.exceptions import HTTPException
from ..models.items import ItemRead, Items, ItemCreate
from ..models.user_items import UserItems


def create_item(session: Session, item: ItemCreate):
    db_item = Items(**item.dict())
    already_exists = session.exec(select(Items).where(Items.name == db_item.name)).first()
    if already_exists:
        raise HTTPException(status_code=400, detail="item already exists")
    session.add(db_item)
    session.commit()
    session.refresh(db_item)
    return db_item

def read_items(session: Session):
    items = session.exec(select(Items)).all()
    if items == []:
        raise HTTPException(status_code=200, detail="items is empty")
    return items

def read_item_by_id(session: Session, item_id: int):
    db_item = session.get(Items, item_id)
    if not db_item:
        raise HTTPException(status_code=404, detail="item not found")
    return db_item

def update_item(session: Session, item_id: int, item: ItemRead):
    db_item = session.get(Items, item_id)
    if not db_item:
        raise HTTPException(status_code=404, detail="item not found")
    item_data = item.dict(exclude_unset=True)
    for key, value in item_data.items():
        setattr(db_item, key, value)
    session.add(db_item)
    session.commit()
    session.refresh(db_item)
    return db_item

def destroy_item(session: Session, item_id: int):
    item = session.get(Items, item_id)
    if not item:
        raise HTTPException(status_code=404, detail="item not found")
    session.delete(item)
    session.commit()
    return {"messate": "item deleted successfully"}
