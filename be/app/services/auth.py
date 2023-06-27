from datetime import datetime, timedelta
from sqlmodel import Session, select
from fastapi import Depends, HTTPException
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

def login(session: Session, username: str, password: str):
    # check if user exist sqlmodel
    user = session.exec(select(Users).where(Users.username == username)).first()
    if not user:
        return HTTPException(status_code=400, detail="Incorrect username or password")
    # check if password match
    if not pwd_context.verify(password, user.password):
        return HTTPException(status_code=400, detail="Incorrect username or password")
    # select from 2 tables role and users to get role name
    role = session.exec(select(Roles.name).where(Roles.role_id == user.role_id)).first()
    print(role)
    if not role:
        return HTTPException(status_code=400, detail="Incorrect username or password")

    # return user
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
