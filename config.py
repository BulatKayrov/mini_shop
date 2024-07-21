from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    class Config:
        env_file = ".env"

    # JWT
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int

    # Database
    DEVELOPMENT: bool
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    DB_HOST: str
    DB_PORT: int

    # Redis
    REDIS_HOST: str
    REDIS_PORT: int

    # Celery
    BROKER_NAME: str = 'redis'

    # Email
    EMAIL_HOST: str
    EMAIL_PORT: int
    EMAIL_HOST_USER: str
    EMAIL_HOST_PASSWORD: str

    @property
    def SQLALCHEMY_DATABASE_URI(self):
        if self.DEVELOPMENT:
            return f'postgresql+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.POSTGRES_DB}'
        return "sqlite+aiosqlite:///database.sqlite3"

    @property
    def REDIS_URL(self):
        return f"{self.BROKER_NAME}://{self.REDIS_HOST}:{self.REDIS_PORT}"


settings = Settings()
