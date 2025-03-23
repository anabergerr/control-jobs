import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.database import SessionLocal, engine
from app.models import Base, Job
from datetime import datetime

# Cria o cliente de teste
client = TestClient(app)

# Fixture para configurar o banco de dados de teste
@pytest.fixture(scope="function")  #"function" para garantir que as tabelas sejam criadas antes de cada teste
def setup_db():
    # Cria as tabelas no banco de dados
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    yield db  # Retorna o banco de dados configurado

    # Limpa o banco de dados após os testes
    db.close()
    Base.metadata.drop_all(bind=engine)

def test_create_job(setup_db):
    # Define o payload (dados) para a requisição POST
    payload = {
        "name_job": "Desenvolvedor Backend",
        "sequence_job": "12345",
        "name_company": "Tech Solutions",
        "result_job": "Projeto concluído com sucesso",
        "obs_job": "Trabalho remoto, entregas semanais",
        "date": "2023-10-05T14:30:00",  # Converte a string para datetime
    }

    # Faz uma requisição POST para a rota /jobs/
    response = client.post("/jobs/", json=payload)

    # Verifica se a resposta tem o status code 200 (OK)
    assert response.status_code == 200

    # Verifica se a mensagem de sucesso está presente na resposta
    data = response.json()
    assert data["message"] == "Job created successfully!"

    # Verifica se o Job foi realmente criado no banco de dados
    db = setup_db
    job = db.query(Job).filter(Job.name_job == "Desenvolvedor Backend").first()
    assert job is not None
    assert job.sequence_job == "12345"
    assert job.name_company == "Tech Solutions"
    assert job.result_job == "Projeto concluído com sucesso"
    assert job.obs_job == "Trabalho remoto, entregas semanais"