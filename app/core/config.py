from dotenv import load_dotenv

import os

load_dotenv()

class Settings:

    DATABASE_URL = os.getenv("DATABASE_URL")
    SECRET_KEY = os.getenv("SECRET_KEY")
    ALGORITHM = os.getenv("ALGORITHM")
    ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES",30))
    RESERVATION_TIMEOUT_MINUTES = int(os.getenv("RESERVATION_TIMEOUT_MINUTES", 1))

settings = Settings()