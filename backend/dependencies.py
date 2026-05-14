# role-based access control
from fastapi import Header, HTTPException
from auth import verify_token

def get_current_user(x_token: str = Header(...)):
    try:
        payload = verify_token(x_token)
        return payload
    except:
        raise HTTPException(status_code=401, detail="Invalid token")