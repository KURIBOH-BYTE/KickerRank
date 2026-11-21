import os

from dotenv import load_dotenv
from sqlalchemy import URL

load_dotenv()

DATABASE_URL = URL.create(
    "mysql+pymysql",
    username=os.getenv("DB_USER", "kicker"),
    password=os.getenv("DB_PASSWORD", "kicker"),
    host=os.getenv("DB_HOST", "localhost"),
    port=int(os.getenv("DB_PORT", "3306")),
    database=os.getenv("DB_NAME", "kickerrank"),
)
