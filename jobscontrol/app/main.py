from fastapi import FastAPI

from app.database import engine  # Importação da engine do banco de dados
from app.models import Base  # Importação dos modelos
from app.routes.jobs import router as jobs_router  # Importação das rotas de jobs

# Cria as tabelas no banco de dados (se não existirem)
Base.metadata.create_all(bind=engine)

# Inicializa a aplicação FastAPI
app = FastAPI()

# Registra as rotas de jobs
app.include_router(jobs_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
