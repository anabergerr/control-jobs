from fastapi import FastAPI
from adapters.web.job_routes import router as jobs_router
from database.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(jobs_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)