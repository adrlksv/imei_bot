from fastapi import HTTPException, status


class ImeiException(HTTPException):
    status_code = 500
    detail = ""

    def __init__(self):
        super().__init__(status_code=self.status_code, detail=self.detail)

class UserAlreadyExistsException(ImeiException):
    status_code = status.HTTP_409_CONFLICT
    detail = "User already exists"

class IncorrectEmailOrPasswordException(ImeiException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Incorrect email or password"

class TokenExpiredException(ImeiException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "The token has expired"

class TokenAbsentException(ImeiException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "The token is missing"

class IncorrectTokenFormatException(ImeiException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Incorrect token format"

class UserIsNotPresentException(ImeiException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = ""
    
class IncorrectImeiFormatException(ImeiException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Incorrect Imei format"
