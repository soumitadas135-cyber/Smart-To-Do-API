import os
from datetime import datetime, timedelta
from jose import jwt
from passlib.context import CryptContext
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY", "smarttodo_super_secret_key_123")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_HOURS = 2

pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)

# -------------------------
# PASSWORD FUNCTIONS
# -------------------------
def hash_password(password: str) -> str:
    if not password or not isinstance(password, str):
        raise ValueError("Invalid password")

    password = password.strip()[:72]   # ✅ truncate STRING (not bytes)
    return pwd_context.hash(password)

def verify_password(password: str, hashed: str) -> bool:
    password = password.strip()[:72]
    return pwd_context.verify(password, hashed)

# -------------------------
# JWT TOKEN
# -------------------------
def create_token(data: dict) -> str:
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(hours=ACCESS_TOKEN_EXPIRE_HOURS)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)