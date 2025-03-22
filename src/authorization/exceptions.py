from src.system.exceptions import JWTError, APIError

class SingatureExpired(JWTError):
  pass

class InvalidToken(JWTError):
  pass

class IncorrectCredentials(APIError):
  pass

class UserAlreadyExists(APIError):
  pass
