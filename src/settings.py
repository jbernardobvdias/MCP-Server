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

    db_enabled: bool = False
    db_postgres_user: SecretStr | None = None
    db_postgres_password: SecretStr | None = None
    db_postgres_db: str | None = None
    db_postgres_host: str | None = None
    db_postgres_port: int = 5432

    model_config = SettingsConfigDict(
        env_file=".env",
        env_prefix="MCP_",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    @property
    def db_url(self) -> URL | None:
        if not self.db_enabled or not all([
            self.db_postgres_user,
            self.db_postgres_password,
            self.db_postgres_db,
            self.db_postgres_host,
        ]):
            return None

        return URL.build(
            scheme="postgresql+asyncpg",
            user=self.db_postgres_user.get_secret_value(),
            password=self.db_postgres_password.get_secret_value(),
            host=self.db_postgres_host,
            port=self.db_postgres_port,
            path=f"/{self.db_postgres_db}",
        )


settings = Settings()