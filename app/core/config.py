from pydantic import BaseSettings


class Settings(BaseSettings):
    API_NAME: str = "Valorant VLR.gg Scraper API"
    API_VERSION: str = "0.1.0"

    HTTP_TIMEOUT: int = 10
    VLR_URL: str = "https://www.vlr.gg"

    class Config:
        env_file = ".env"


settings = Settings()