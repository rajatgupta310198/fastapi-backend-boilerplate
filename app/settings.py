import os


class AppConfigSettings:
    REDIS_HOST = os.getenv('REDIS_HOST')
    REDIS_PORT = os.getenv('REDIS_PORT')
    POSTGRES_DATABASE_URL = os.getenv('POSTGRES_DATABASE_URL')
    JWT_REGEX = os.getenv('JWT_REGEX')
    JWT_ALGO = os.getenv('JWT_ALGO')
    ACCESS_SECRET = os.getenv('ACCESS_SECRET')
    REFRESH_SECRET = os.getenv('REFRESH_SECRET')


