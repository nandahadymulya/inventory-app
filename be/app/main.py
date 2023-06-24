from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlmodel import SQLModel, Session
from .configs.database import engine
from .services.roles import read_roles, read_role_by_id
from .services.users import read_users, read_user_by_id
from .services.items import read_items, read_item_by_id
from .models.roles import Roles as RolesModel, RolesRead
from .models.users import Users as UsersModel, UserRead
from .models.items import Items as ItemsModel, ItemRead, ItemCreate as ItemCreateModel

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

app = FastAPI(
    title="FastAPI Inventory App",
    description="A simple Inventory App API built with FastAPI",
    author="Nanda Hady Mulya",
)


# cors
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


@app.on_event("startup")
def on_startup():
    create_db_and_tables()

@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this fantastic app!"}


def get_session():
    with Session(engine) as session:
        yield session

# Auth API
@app.post("/auth/register", tags=["Auth"], description="Register user")
async def post_register():
    pass

@app.post("/auth/login", tags=["Auth"], description="Login to get token")
async def post_login():
    pass

@app.post("/auth/logout", tags=["Auth"], description="Logout from token")
async def post_logout():
    pass

# Roles API
@app.get("/roles/", response_model=list[RolesModel], tags=["Roles"], description="Get all roles")
async def get_roles(offset: int = 0, limit: int = 100, session: Session = Depends(get_session)):
    roles = read_roles(session, offset, limit)
    return roles

@app.get("/roles/{role_id}", response_model=RolesRead, tags=["Roles"], description="Get role by id")
async def get_roles(role_id: int, session: Session = Depends(get_session)):
    roles = read_role_by_id(session, role_id)
    return roles

@app.post("/roles/", response_model=list[RolesModel], tags=["Roles"], description="Post new role")
async def post_role():
    pass

@app.patch("/roles/{role_id}", response_model=list[RolesModel], tags=["Roles"], description="Patch role by id")
async def patch_role():
    pass

@app.delete("/roles/{role_id}", response_model=list[RolesModel], tags=["Roles"], description="Delete role by id")
async def delete_role():
    pass

# Users API
@app.get("/users/", response_model=list[UsersModel], tags=["Users"], description="Get all users")
async def get_users(offset: int = 0, limit: int = 100, session: Session = Depends(get_session)):
    users = read_users(session, offset, limit)
    return users

@app.get("/users/{user_id}", response_model=UserRead, tags=["Users"], description="Get user by id")
async def get_user_by_id(user_id: int, session: Session = Depends(get_session)):
    user = read_user_by_id(session=session, user_id=user_id)
    return user

@app.patch("/users/{user_id}", response_model=list[RolesModel], tags=["Users"], description="Patch user by id")
async def patch_user():
    pass

@app.delete("/users/{user_id}", response_model=list[RolesModel], tags=["Users"], description="Delete user by id")
async def delete_user():
    pass

# Items API
@app.get("/items/", response_model=list[ItemsModel], tags=["Items"], description="Get all items")
async def get_items(session: Session = Depends(get_session)):
    items = read_items(session)
    return items

@app.get("/items/{item_id}", response_model=ItemRead, tags=["Items"], description="Get item by id")
async def get_item_by_id(item_id: int, session: Session = Depends(get_session)):
    item = read_item_by_id(session=session, item_id=item_id)
    return item

@app.post("/items/", response_model=ItemRead, tags=["Items"], description="Post new item")
async def post_item(*, session: Session = Depends(get_session), item: ItemCreateModel):
    pass

@app.patch("/items/{item_id}", response_model=list[RolesModel], tags=["Items"], description="Patch item by id")
async def patch_item():
    pass

@app.delete("/items/{item_id}", response_model=list[RolesModel], tags=["Items"], description="Delete item by id")
async def delete_item():
    pass
