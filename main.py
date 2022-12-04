from dotenv import load_dotenv


from app.app import create_app


# load_settings()
load_dotenv()


app = create_app()
