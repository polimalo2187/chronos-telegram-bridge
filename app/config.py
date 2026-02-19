from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=None, extra="ignore")

    BOT_TOKEN: str
    API_BASE_URL: str
    TELEGRAM_LINK_SECRET: str


settings = Settings()
