import os


from dotenv import load_dotenv

 

def load_settings():
    print("Loading settings...")
    
    load_dotenv(dotenv_path=os.getcwd() + "/.env")


class AppConfigSettings:
    REDIS_HOST = os.getenv('REDIS_HOST')
    REDIS_PORT = os.getenv('REDIS_PORT')
    POSTGRES_DATABASE_URL = os.getenv('POSTGRES_DATABASE_URL')


