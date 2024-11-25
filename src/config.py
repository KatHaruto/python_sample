from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class Config(BaseSettings):
    model_config = SettingsConfigDict()

    OPENAI_API_KEY: SecretStr


config = Config()  # type: ignore[call-arg]
