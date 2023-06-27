from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse
from jose import jwt, JWTError
from ..configs.environment import get_environment_variables


env = get_environment_variables()
SECRET_KEY = f"{env.SECRET_KEY}"
ALGORITHM = "HS256"

async def token_middleware(request: Request, call_next):
    token = request.headers.get("Authorization")

    if token:
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            username: str = payload.get("username")
            role: str = payload.get("role")
            if not username:
                raise HTTPException(status_code=401, detail="Invalid authentication credentials")
            if not role:
                raise HTTPException(status_code=401, detail="Invalid authentication credentials")
            request.state.user = username
            request.state.role = role
            response = await call_next(request)
            return response
        except JWTError:
            raise HTTPException(status_code=401, detail="Invalid authentication credentials")

    return JSONResponse(status_code=401, content={"message": "Unauthorized"})
