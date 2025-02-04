from fastapi import APIRouter, Depends

from src.backend.users.dependencies import get_current_user
from src.backend.imei_ckeck.imei_service import get_imei

from src.backend.imei_ckeck.schemas import SImeiRequest

from src.backend.users.models import User


router = APIRouter(
    prefix="/check-imei",
    tags=["Check imei"]
)


@router.post("/")
async def get_imei_info(
    imei: SImeiRequest,
    user: User = Depends(get_current_user)
):
    imei_data = await get_imei(imei.imei)

    return imei_data
