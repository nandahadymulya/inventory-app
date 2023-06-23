from fastapi import Depends, FastAPI, HTTPException
from sqlmodel import SQLModel, Session
from .configs.database import engine
from .services.roles import read_roles
from .services.users import read_users
from .services.items import read_items
from .models.roles import Roles as RolesModel
from .models.users import Users as UsersModel
from .models.items import Items as ItemsModel


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

app = FastAPI(
    title="FastAPI Inventory",
    description="A simple inventory API built with FastAPI",
    author="Nanda Hady Mulya",
)

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this fantastic app!"}


def get_session():
    with Session(engine) as session:
        yield session

@app.get("/roles/", response_model=list[RolesModel], tags=["Roles"], description="Get all roles")
async def get_roles(offset: int = 0, limit: int = 100, session: Session = Depends(get_session)):
    roles = read_roles(session, offset, limit)
    return roles

@app.get("/users/", response_model=list[UsersModel], tags=["Users"], description="Get all users")
async def get_users(offset: int = 0, limit: int = 100, session: Session = Depends(get_session)):
    users = read_users(session, offset, limit)
    return users

@app.get("/items/", response_model=list[ItemsModel], tags=["Items"], description="Get all items")
async def get_items(session: Session = Depends(get_session)):
    items = read_items(session)
    return items
