from datetime import datetime
import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.database import SessionLocal, engine
from app.models import Base, Job

# Cria o cliente de teste
client = TestClient(app)

# Fixture para configurar o banco de dados de teste
@pytest.fixture(scope="module")
def setup_db():
    # Cria as tabelas no banco de dados
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()

    # Cria um job de exemplo para os testes
    job = Job(
        name_job='Desenvolvedor Backend',
        sequence_job='12345',
        name_company='Tech Solutions',
        result_job='Projeto concluído com sucesso',
        obs_job='Trabalho remoto, entregas semanais',
        date=datetime.fromisoformat("2023-10-05T14:30:00"),
    )
    db.add(job)
    db.commit()

    yield db  # Retorna o banco de dados configurado

    # Limpa o banco de dados após os testes
    db.close()
    Base.metadata.drop_all(bind=engine)

def test_update_job_partial_success(setup_db):
    # Define o payload para a requisição PATCH
    payload = {
        "name_job": "Desenvolvedor Frontend",  # Atualiza apenas o nome do job
    }

    # Faz uma requisição PATCH para atualizar o job com id 1
    response = client.patch("/jobs/1", json=payload)

    # Verifica se a resposta tem o status code 200 (OK)
    assert response.status_code == 200

    # Verifica se o job foi atualizado corretamente
    updated_job = response.json()
    assert updated_job["name_job"] == "Desenvolvedor Frontend"