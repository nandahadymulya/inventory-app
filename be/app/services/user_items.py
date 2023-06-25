from fastapi import HTTPException, Depends, Query
from sqlmodel import Session, select
from ..models.items import Items
from ..models.users import Users
from ..models.user_items import UserItems


def read_user_items(session: Session):
    userItems = session.exec(select(UserItems)).all()
    # read useritems by user_id
    # for userItem in userItems:

    # userItems = session.exec(select(UserItems).where(UserItems.user_id == 1)).all()
    # user = session.exec(select(Users)).all()

    # for userItem in userItems:
    #     user = session.get(Users, userItem.user_id)
    #     item = session.get(Items, userItem.item_id)
    #     print(user)
    #     print(item)
    # #  for user_id is same
    # for userItem in userItems:
    #     user = session.get(Users, userItem.user_id)

    # user_id = session.get(Users, userItems[0].user_id)
    # for userItem in userItems:
    #     user = session.get(Users, userItem.user_id)
    #     item = session.get(Items, userItem.item_id)
    #     detail_items.append({
    #         'item': item
    #     })
    # return detail_items
