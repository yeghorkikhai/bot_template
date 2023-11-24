from os.path import abspath
from os import getenv

from dotenv import load_dotenv

from dataclasses import dataclass

load_dotenv(abspath(".env"))


@dataclass(frozen=True)
class AppConfig:

    telegram_token: str = getenv("TELEGRAM_TOKEN")
    telegram_secret_token: str = getenv("TELEGRAM_SECRET_TOKEN")

    base_url: str = getenv("BASE_URL")
    webhook_path: str = getenv("WEBHOOK_PATH")

    host: str = getenv("APP_HOST")
    port: int = getenv("APP_PORT")
