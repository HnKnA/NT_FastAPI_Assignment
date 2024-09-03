import os
from dotenv import load_dotenv

load_dotenv()

def get_connection_string(asyncMode: bool = False) -> str:
    engine = os.getenv("DB_ENGINE") if not asyncMode else os.getenv("ASYNC_DB_ENGINE")
    username = os.getenv("DB_USERNAME")
    password = os.getenv("DB_PASSWORD")
    dbhost = os.getenv("DB_HOST")
    dbport = os.getenv("DB_PORT")
    dbname = os.getenv("DB_NAME")
    return f"{engine}://{username}:{password}@{dbhost}:{dbport}/{dbname}"

# Database settings
SQLALCHEMY_DB_URL = get_connection_string()
SQLALCHEMY_DB_URL_ASYNC = get_connection_string(asyncMode=True)

ADMIN_DEFAULT_PASSWORD = os.getenv("ADMIN_DEFAULT_PASSWORD")

# JWT settings
JWT_SECRET = os.getenv("JWT_SECRET")
JWT_ALGORITHM = os.getenv("JWT_ALGORITHM")