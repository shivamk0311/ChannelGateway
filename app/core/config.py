from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):

    APP_NAME: str = "Channel Gateway"
    ENVIRONMENT: str = "development"
    DEBUG: bool = False

    DATABASE_HOST : str = "localhost"
    DATABASE_PORT : int = 5434
    DATABASE_USER : str = "channel"
    DATABASE_PASSWORD : str = "channel"
    DATABASE_NAME : str ="channel_gateway"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8"
    )

    @property
    def database_url(self) -> str:
        return (
            f"postgresql+psycopg://"
            f"{self.DATABASE_USER}:{self.DATABASE_PASSWORD}"
            f"@{self.DATABASE_HOST}:{self.DATABASE_PORT}"
            f"/{self.DATABASE_NAME}"
        )
settings = Settings()