from fastapi import FastAPI





def create_app() -> FastAPI:


    
    
    app = FastAPI(title="User Service API",
    
        )




    

    # include all routes here
    from app.users.routes import user_api

    app.include_router(user_api)



    return app