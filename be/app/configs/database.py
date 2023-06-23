from sqlmodel import create_engine
from .environment import get_environment_variables

env = get_environment_variables()

DATABASE_URL = f"{env.DATABASE_TYPE}://{env.DATABASE_USERNAME}:{env.DATABASE_PASSWORD}@{env.DATABASE_HOSTNAME}:{env.DATABASE_PORT}/{env.DATABASE_NAME}"

engine = create_engine(
    DATABASE_URL, echo=env.DEBUG_MODE
)

def get_engine():
    return engine
# SessionLocal = sessionmaker(autocommit=False, autoflush=True, bind=engine, future=True)
# Base = declarative_base()
