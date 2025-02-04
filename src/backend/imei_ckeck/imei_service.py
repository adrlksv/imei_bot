import httpx
from src.backend.config import settings


async def get_imei(imei: str):
    url = "https://api.imeicheck.net/v1/orders/precheck"
    payload = {
        "deviceIds": [imei],
        "serviceId": 12,
        "duplicateProcessingType": "reprocess"
    }
    headers = {
        'Authorization': f'Bearer {settings.TOKEN_SANDBOX}',
        'Accept-Language': 'en',
        'Content-Type': 'application/json'
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(url, headers=headers, json=payload)
    
    return response.json()
