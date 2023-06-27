from sqlmodel import SQLModel, create_engine
from .environment import get_environment_variables


env = get_environment_variables()

DATABASE_URL = f"{env.DATABASE_TYPE}://{env.DATABASE_USERNAME}:{env.DATABASE_PASSWORD}@{env.DATABASE_HOSTNAME}:{env.DATABASE_PORT}/{env.DATABASE_NAME}"

engine = create_engine(
    DATABASE_URL, echo=env.DEBUG_MODE
)

def get_engine():
    return engine

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def drop_db_and_tables():
    SQLModel.metadata.drop_all(engine)
