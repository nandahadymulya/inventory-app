from typing import Annotated, Union
from datetime import datetime, timedelta
from sqlmodel import Session, select
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext
from ..models.auth import TokenData
from ..models.roles import Roles
from ..models.users import Users
from ..configs.environment import get_environment_variables


env = get_environment_variables()
SECRET_KEY = f"{env.SECRET_KEY}"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")


def hash_password(password: str):
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)


def authenticate_user(session: Session, username: str, password: str):
    user = session.exec(select(Users).where(Users.username == username)).first()
    if not user:
        return HTTPException(status_code=400, detail="Incorrect username or password")
    password_is_valid = verify_password(password, user.password)
    if not password_is_valid:
        return HTTPException(status_code=400, detail="Incorrect username or password")
    role = session.exec(select(Roles.name).where(Roles.role_id == user.role_id)).first()
    if not role:
        return HTTPException(status_code=400, detail="Incorrect username or password")
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"username": user.username, "role": role}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

def create_access_token(data: dict, expires_delta: timedelta = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)):
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=401,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"}
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("username")
        role: str = payload.get("role")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username, role=role)
    except JWTError:
        raise credentials_exception
    return token_data


# async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
#     credentials_exception = HTTPException(
#         status_code=status.HTTP_401_UNAUTHORIZED,
#         detail="Could not validate credentials",
#         headers={"WWW-Authenticate": "Bearer"},
#     )
#     try:
#         payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
#         username: str = payload.get("username")
#         role: str = payload.get("role")
#         if username is None:
#             raise credentials_exception
#         token_data = TokenData(username=username, role=role)
#     except JWTError:
#         raise credentials_exception

#     user = get_user(token_data.username)
#     if user is None:
#         raise credentials_exception
#     return user

async def get_current_active_user(
    current_user: Annotated[Users, Depends(get_current_user)]
):
    if not current_user:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user

def login(session: Session, credentials: Annotated[OAuth2PasswordRequestForm, Depends()]):
    user = authenticate_user(session, credentials.username, credentials.password)
    return user
