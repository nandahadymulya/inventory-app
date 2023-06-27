from typing import Annotated
from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordRequestForm
from sqlmodel import SQLModel, Session
from .configs.database import engine
from .services.auth import login, get_current_user
from .services.roles import create_role, read_roles, read_role_by_id, update_role, destroy_role
from .services.users import create_user, read_users, read_user_by_id, update_user, destroy_user
from .services.items import create_item, read_items, read_item_by_id,update_item, destroy_item
from .models.roles import RoleRead
from .models.users import UserRead, UserCreate
from .models.items import ItemRead, ItemCreate

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

app = FastAPI(
    title="FastAPI Inventory App",
    description="A simple Inventory App API built with FastAPI and SQLModel",
    author="Nanda Hady Mulya",
)

origins = [
    "*",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_session():
    with Session(bind=engine) as session:
        yield session

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to Inventory App!"}

# Auth API
@app.post("/auth/register", response_model=UserCreate, tags=["Auth"], description="Register user")
async def post_register(user: UserCreate, session: Session = Depends(get_session)):
    registered_user = create_user(session, user)
    return registered_user


@app.post("/auth/login", tags=["Auth"], description="Login to get token")
async def post_login(credential: Annotated[OAuth2PasswordRequestForm, Depends()], session: Session = Depends(get_session)):
    isUserLoggedIn = login(session, credential)
    return isUserLoggedIn

@app.get("/auth/me", tags=["Auth"], description="Get current user with token")
async def get_me(token: str):
    current_user = get_current_user(token)
    return current_user

@app.post("/auth/logout", tags=["Auth"], description="Logout from token")
async def post_logout():
    pass

# Roles API
@app.get("/roles/", response_model=list[RoleRead], tags=["Roles"], description="Get all roles")
async def get_roles(offset: int = 0, limit: int = 100, session: Session = Depends(get_session)):
    roles = read_roles(session, offset, limit)
    return roles

@app.get("/roles/{role_id}", response_model=RoleRead, tags=["Roles"], description="Get role by id")
async def get_roles(role_id: int, session: Session = Depends(get_session)):
    roles = read_role_by_id(session, role_id)
    return roles

@app.post("/roles/", response_model=RoleRead, tags=["Roles"], description="Post new role")
async def post_role(role: RoleRead, session: Session = Depends(get_session)):
    created_role = create_role(session, role)
    return created_role

@app.patch("/roles/{role_id}", response_model=RoleRead, tags=["Roles"], description="Patch role by id")
async def patch_role(role_id: int, role: RoleRead, session: Session = Depends(get_session)):
    updated_role = update_role(session, role_id, role)
    return updated_role

@app.delete("/roles/{role_id}", tags=["Roles"], description="Delete role by id")
async def delete_role(role_id: int, session: Session = Depends(get_session)):
    deleted_role = destroy_role(session, role_id)
    return deleted_role

# Users API
@app.get("/users/", response_model=list[UserRead], tags=["Users"], description="Get all users")
async def get_users(offset: int = 0, limit: int = 100, session: Session = Depends(get_session)):
    users = read_users(session, offset, limit)
    return users

@app.get("/users/{user_id}", response_model=UserRead, tags=["Users"], description="Get user by id")
async def get_user_by_id(user_id: int, session: Session = Depends(get_session)):
    user = read_user_by_id(session=session, user_id=user_id)
    return user

@app.patch("/users/{user_id}", response_model=UserRead, tags=["Users"], description="Patch user by id")
async def patch_user(user_id: int, user: UserRead, session: Session = Depends(get_session)):
    updated_user = update_user(session, user_id, user)
    return updated_user

@app.delete("/users/{user_id}", tags=["Users"], description="Delete user by id")
async def delete_user(user_id: int, session: Session = Depends(get_session)):
    deleted_user = destroy_user(session, user_id)
    return deleted_user

# Items API
@app.get("/items/", response_model=list[ItemRead], tags=["Items"], description="Get all items")
async def get_items(session: Session = Depends(get_session)):
    items = read_items(session)
    return items

@app.get("/items/{item_id}", response_model=ItemRead, tags=["Items"], description="Get item by id")
async def get_item_by_id(item_id: int, session: Session = Depends(get_session)):
    item = read_item_by_id(session=session, item_id=item_id)
    return item

@app.post("/items/", response_model=ItemCreate, tags=["Items"], description="Post new item")
async def post_item(item: ItemCreate, session: Session = Depends(get_session)):
    item = create_item(session=session, item=item)
    return item

@app.patch("/items/{item_id}", response_model=ItemRead, tags=["Items"], description="Patch item by id")
async def patch_item(item_id: int, item: ItemRead, session: Session = Depends(get_session)):
    upadted_item = update_item(session=session, item_id=item_id, item=item)
    return upadted_item

@app.delete("/items/{item_id}", tags=["Items"], description="Delete item by id")
async def delete_item(item_id: int, session: Session = Depends(get_session)):
    item = destroy_item(session=session, item_id=item_id)
    return item
