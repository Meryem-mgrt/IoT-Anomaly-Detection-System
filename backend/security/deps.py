from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from backend.security.jwt import decode_token

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

def get_current_user(token: str = Depends(oauth2_scheme)):

    try:
        payload = decode_token(token)
        return {
            "username": payload.get("sub"),
            "role": payload.get("role")
        }

    except:
        raise HTTPException(status_code=401, detail="Invalid token")