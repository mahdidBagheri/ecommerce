import os

APP_ENV = os.getenv("APP_ENV", "development")
DATABASE_USERNAME = os.getenv("DATABASE_USERNAME", "postgres")
DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD", "pass")
DATABASE_HOST = os.getenv("DATABASE_HOST", "Localhost:5431")
DATABASE_NAME = os.getenv("DATABASE_NAME", "fastapi_database")
TEST_DATABASE_NAME = os.getenv("DATABASE_NAME", "ecommerce_test")
