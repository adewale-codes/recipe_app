from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql://postgres:*abi1oLA@localhost:5432/recipe"

    class Config:
        env_file = ".env"

settings = Settings()
