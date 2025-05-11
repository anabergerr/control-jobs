from fastapi import FastAPI

from adapters.web.job_routes import router as jobs_router
from adapters.web.auth_routes import router as auth_router
from adapters.web.user_routes import router as user_router
from database.database import Base, engine


Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(jobs_router)
app.include_router(auth_router)
app.include_router(user_router)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
