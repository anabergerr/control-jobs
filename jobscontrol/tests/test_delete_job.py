from datetime import datetime
import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.database import SessionLocal, engine
from app.models import Base, Job
from sqlalchemy.exc import IntegrityError

# Cria o cliente de teste
client = TestClient(app)

# Fixture para configurar o banco de dados de teste
@pytest.fixture(scope="function")
def setup_db():
    # Cria as tabelas no banco de dados
    Base.metadata.drop_all(bind=engine)  # Limpa o banco antes de recriar
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()

    # Cria dois jobs com a estrutura desejada
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
    db.refresh(job1)
    db.refresh(job2)

    yield db  # Retorna o banco de dados configurado

    # Limpa o banco de dados após os testes
    db.close()
    Base.metadata.drop_all(bind=engine)

# Teste onde o Job ID não é informado
def test_delete_job_not_provided():
    response = client.delete("/jobs/")
    assert response.status_code == 405  # Espera-se 405, pois a rota "/jobs/" existe, mas não para DELETE
    assert response.json()['detail'] == 'Method Not Allowed'

# Teste onde o Job não é encontrado
def test_delete_job_not_found(setup_db):
    # Faz uma requisição DELETE para um job_id que não existe
    response = client.delete("/jobs/999")
    json_data = response.json()
    response_code = 404

    # Verifica se a resposta é 404 (Not Found)
    assert response.status_code == response_code
    assert json_data['detail'] == 'Job not found.'

# Teste onde o Job é excluído com sucesso
def test_delete_job_success(setup_db):
    # Primeiro, exclui o job
    response = client.delete("/jobs/1")
    json_data = response.json()
    response_code = 200
    response_code_nf = 404

    # Verifica se a exclusão do job foi bem-sucedida
    assert response.status_code == response_code
    assert json_data['message'] == "Job deleted."

    # Em seguida, tenta excluir o job novamente e verifica se retorna 404
    # Já que o job foi excluído, a segunda tentativa deve resultar em erro 404
    response = client.delete("/jobs/1")
    json_data = response.json()

    # Verifica se o código de status é 404 (não encontrado) e a mensagem correta
    assert response.status_code == response_code_nf
    assert json_data['detail'] == 'Job not found.'