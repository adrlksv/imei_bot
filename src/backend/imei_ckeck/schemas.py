from pydantic import BaseModel, validator

from src.backend.exceptions import IncorrectImeiFormatException


class SImeiRequest(BaseModel):
    imei: str

    @validator("imei")
    def validate_imei(cls, imei):
        if not len(imei) == 15:
            raise IncorrectImeiFormatException
        return imei
