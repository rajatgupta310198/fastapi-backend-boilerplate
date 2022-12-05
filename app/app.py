from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware




def create_app() -> FastAPI:


    
    
    app = FastAPI(title="User Service API",
    
        )

    app.add_middleware(
        CORSMiddleware,
        allow_headers=["*"],
    )



    

    # include all routes here
    from app.users.routes import user_api
    from app.users.routes import auth_api

    app.include_router(user_api)
    app.include_router(auth_api)



    return app