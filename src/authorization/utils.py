import jwt
import bcrypt
from pathlib import Path
from .config import settings
from datetime import datetime
from .exceptions import SingatureExpired, InvalidToken

def encode_jwt(payload: dict, exp_time: int | str = 3600) -> str:
    try:
        if not isinstance(payload, dict):
            raise ValueError("Payload must be a dictionary")

        if isinstance(exp_time, str):
            try:
                exp_time = int(exp_time)
            except ValueError:
                raise ValueError("exp_time must be a valid integer or string representation of an integer")
        
        expire_date = datetime.timestamp(datetime.now()) + exp_time
        payload.update({"exp": expire_date})
        
        try:
            encoded = jwt.encode(
                payload=payload,
                key=Path(settings.PRIVATE_KEY).read_text(), 
                algorithm=settings.ALGORITHM
            )
            return encoded
        except FileNotFoundError:
            raise RuntimeError("Private key file not found")
        except jwt.InvalidKeyError:
            raise RuntimeError("Invalid private key format")
        except Exception as e:
            raise RuntimeError(f"JWT encoding failed: {str(e)}")

    except Exception as e:
        raise RuntimeError(f"Error in JWT encoding process: {str(e)}")

def decode_jwt(token: str) -> dict:
  try:
    decoded = jwt.decode(token, key=(Path(settings.PUBLIC_KEY).read_text()), 
               algorithms=[settings.ALGORITHM])
    return decoded

  except jwt.ExpiredSignatureError:
    raise SingatureExpired
  except jwt.InvalidTokenError:
    raise InvalidToken
  # except Exception as e:
  #   raise RuntimeError(f"Error decoding JWT: {e}")


def hash_password(password: str) -> bytes:
    try:
        pwd_bytes = password.encode('utf-8')
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password=pwd_bytes, 
                                        salt=salt)
        return hashed_password
    except Exception as e:
        raise (f"Error hashing password: {e}")


def verify_password(hashed_password: bytes, 
                        password: str) -> bool:
  return bcrypt.checkpw(password.encode('utf-8'), 
                              hashed_password)



def encrypt_private_key():
   ...