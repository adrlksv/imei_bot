from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    TOKEN_BOT: str

    API_URL: str
    LOGIN_URL: str
    REGISTER_URL: str
    ME_URL: str
    LOGOUT_URL: str
    IMEI_CHECK_URL: str

    TOKEN_SANDBOX: str

    SECRET_KEY: str
    ALGORITHM: str

    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASS: str
    DB_NAME: str

    @property
    def DATABASE_URL(self):
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    class Config:
        env_file = ".env"


settings = Settings()
