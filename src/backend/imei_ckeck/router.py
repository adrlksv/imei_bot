from fastapi import APIRouter

from src.backend.imei_ckeck.imei_service import get_imei
from src.backend.imei_ckeck.schemas import SImeiRequest



router = APIRouter(
    prefix="/check-imei",
    tags=["Check imei"]
)


@router.post("/")
async def get_imei_info(
    imei: SImeiRequest
):
    imei_data = await get_imei(imei.imei)

    return imei_data
