# JWT authentication
from jose import jwt, JWTError
from fastapi import Header, HTTPException

SECRET = "CHANGE_THIS_SECRET"
ALGO = "HS256"

def verify_token(x_token: str = Header(...)):

    try:
        payload = jwt.decode(x_token, SECRET, algorithms=[ALGO])
        return payload

    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")