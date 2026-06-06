from dotenv import load_dotenv

import os

load_dotenv()

class Settings:

    DATABASE_URL = os.getenv("DATABASE_URL")

    RESERVATION_TIMEOUT_MINUTES = int(os.getenv("RESERVATION_TIMEOUT_MINUTES", 1))

settings = Settings()