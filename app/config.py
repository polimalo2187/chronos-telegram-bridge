from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    BOT_TOKEN: str
    API_BASE_URL: str
    TELEGRAM_LINK_SECRET: str

settings = Settings()
