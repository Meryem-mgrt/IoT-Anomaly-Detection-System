import os

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://pfa_user:pfa_pass@localhost:5432/pfa_db"
)