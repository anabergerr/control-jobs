from datetime import datetime
import pytest
from fastapi.testclient import TestClient
from app.main import app  # Importação da aplicação FastAPI
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

    # Adiciona dados de teste
    job1 = Job(
        name_job='Desenvolvedor Backend',
        sequence_job='12345',
        name_company='Tech Solutions',
        result_job='Projeto concluído com sucesso',
        obs_job='Trabalho remoto, entregas semanais',
        date=datetime.fromisoformat("2023-10-05T14:30:00"),
    )

    job2 = Job(
        name_job='Desenvolvedor Frontend',
        sequence_job='67890',
        name_company='Web Innovations',
        result_job='Trabalho em progresso',
        obs_job='Equipe colaborativa',
        date=datetime.fromisoformat("2023-11-15T09:00:00"),
    )

    db.add(job1)
    db.add(job2)
    db.commit()

    yield db  # Retorna o banco de dados configurado

    # Limpa o banco de dados após os testes
    db.close()
    Base.metadata.drop_all(bind=engine)

# Teste para obter todos os jobs
def test_get_jobs(setup_db):
    # Faz uma requisição GET para o endpoint /jobs
    response = client.get("/jobs/")
    json_data = response.json()
    response_code = 200
    expected_jobs = 2

    # Verifica se a resposta é 200 OK
    assert response.status_code == response_code

    # Verifica se o número de jobs retornados está correto
    assert len(json_data) == expected_jobs

    # Verifica os campos do primeiro job
    assert json_data[0]['name_job'] == 'Desenvolvedor Backend'
    assert json_data[0]['sequence_job'] == '12345'
    assert json_data[0]['name_company'] == 'Tech Solutions'
    assert json_data[0]['result_job'] == 'Projeto concluído com sucesso'
    assert json_data[0]['obs_job'] == 'Trabalho remoto, entregas semanais'
    assert json_data[0]['date'] == '2023-10-05T14:30:00'

    # Verifica os campos do segundo job
    assert json_data[1]['name_job'] == 'Desenvolvedor Frontend'
    assert json_data[1]['sequence_job'] == '67890'
    assert json_data[1]['name_company'] == 'Web Innovations'
    assert json_data[1]['result_job'] == 'Trabalho em progresso'
    assert json_data[1]['obs_job'] == 'Equipe colaborativa'
    assert json_data[1]['date'] == '2023-11-15T09:00:00'

# Teste para obter todos os jobs quando o banco de dados está vazio
def test_get_jobs_empty():
    # Limpa o banco de dados antes do teste
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    # Faz uma requisição GET para o endpoint /jobs
    response = client.get("/jobs/")
    json_data = response.json()
    response_code = 200

    # Verifica se a resposta é 200 OK
    assert response.status_code == response_code

    # Verifica se a lista retornada está vazia
    assert len(json_data) == 0