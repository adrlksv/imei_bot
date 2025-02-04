from fastapi import FastAPI

from src.backend.users.router import router as user_router
from src.backend.imei_ckeck.router import router as imei_router


app = FastAPI()

app.include_router(user_router)
app.include_router(imei_router)
