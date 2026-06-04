from typing import Literal

from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict
from yarl import URL


class Settings(BaseSettings):
    transport: str = "http"
    host: str = "0.0.0.0"
    port: int = 8000
    server_name: str = "FastMCP"
    server_instructions: str = ""

    postgres_user: SecretStr | None = None
    postgres_password: SecretStr | None = None
    postgres_db: str | None = None
    postgres_host: str | None = None
    postgres_port: int = 5432

    openai_key: SecretStr | None = None
    embeddings_model: str | None = None

    model_config = SettingsConfigDict(
        env_file=".env",
        env_prefix="",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    @property
    def db_url(self) -> URL | None:
        if not all([
            self.postgres_user,
            self.postgres_password,
            self.postgres_db,
            self.postgres_host,
        ]):
            return None

        return URL.build(
            scheme="postgresql+asyncpg",
            user=self.postgres_user.get_secret_value(),
            password=self.postgres_password.get_secret_value(),
            host=self.postgres_host,
            port=self.postgres_port,
            path=f"/{self.postgres_db}",
        )


settings = Settings()