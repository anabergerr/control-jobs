from datetime import datetime

import pytest

from app import create_app, db
from app.models import Job


# Fixture para configurar o cliente de teste e o banco de dados em memória
@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    with app.app_context():
        db.create_all()  # Cria as tabelas no banco de dados de teste
        yield app.test_client()  # Retorna o cliente de teste
        db.drop_all()  # Limpa o banco de dados após os testes


# Fixture para inicializar o banco de dados com alguns dados
@pytest.fixture
def init_database():
    # Cria dois jobs com a estrutura desejada
    job1 = Job(
        name_job='Desenvolvedor Backend',
        sequence_job='12345',
        name_company='Tech Solutions',
        result_job='Projeto concluído com sucesso',
        obs_job='Trabalho remoto, entregas semanais',
        date=datetime.strptime('2023-10-05T14:30:00', '%Y-%m-%dT%H:%M:%S'),
    )

    job2 = Job(
        name_job='Desenvolvedor Frontend',
        sequence_job='67890',
        name_company='Web Innovations',
        result_job='Trabalho em progresso',
        obs_job='Equipe colaborativa',
        date=datetime.strptime('2023-11-15T09:00:00', '%Y-%m-%dT%H:%M:%S'),
    )

    db.session.add(job1)
    db.session.add(job2)
    db.session.commit()

    yield db  # Retorna o banco de dados com os dados iniciais

    # Limpa o banco após os testes
    db.session.remove()
    db.drop_all()


# Teste onde o Job ID não é informado
def test_delete_job_not_provided(client):
    response = client.delete('/jobs', json={})
    json_data = response.get_json()
    responde_code = 400

    assert response.status_code == responde_code
    assert json_data['error'] == 'Job ID not provided.'


# Teste onde o Job não é encontrado
def test_delete_job_not_found(client):
    response = client.delete('/jobs', json={'id': 999})
    json_data = response.get_json()
    responde_code = 404

    assert response.status_code == responde_code
    assert json_data['error'] == 'Job not found.'


# Teste onde o Job é excluído com sucesso
def test_delete_job_success(client, init_database):
    response = client.delete('/jobs', json={'id': 1})
    json_data = response.get_json()
    responde_code = 200
    responde_code_nf = 404

    assert response.status_code == responde_code
    assert json_data['message'] == 'Job deleted successfully.'

    # Verifica se o job foi realmente excluído
    response = client.delete('/jobs', json={'id': 1})
    json_data = response.get_json()

    assert response.status_code == responde_code_nf
    assert json_data['error'] == 'Job not found.'


# Teste que simula um erro de integridade no banco de dados
def test_delete_job_integrity_error(client, mocker):
    job = Job(
        name_job='Desenvolvedor Backend',
        sequence_job='12345',
        name_company='Tech Solutions',
        result_job='Projeto concluído com sucesso',
        obs_job='Trabalho remoto, entregas semanais',
        date=datetime.strptime('2023-10-05T14:30:00', '%Y-%m-%dT%H:%M:%S'),
    )
    db.session.add(job)
    db.session.commit()

    # Simular um erro de integridade no commit
    mocker.patch(
        'app.models.db.session.commit',
        side_effect=db.exc.IntegrityError(None, None, None),
    )

    response = client.delete('/jobs', json={'id': job.idJob})
    json_data = response.get_json()
    responde_code = 500

    assert response.status_code == responde_code
    assert json_data['error'] == 'Database integrity error while deleting job.'
