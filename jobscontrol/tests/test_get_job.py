from datetime import datetime

import pytest

from app import create_app, db
from app.models import Job


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


@pytest.fixture
def init_database():
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

    yield db

    db.session.remove()
    db.drop_all()


def test_get_jobs(client, init_database):
    # Faz uma requisição GET para o endpoint /jobs
    response = client.get('/jobs')
    json_data = response.get_json()
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


def test_get_jobs_empty(client):
    # Testa o caso em que não há nenhum job no banco de dados
    response = client.get('/jobs')
    json_data = response.get_json()
    response_code = 200

    # Verifica se a resposta é 200 OK
    assert response.status_code == response_code

    # Verifica se a lista retornada está vazia
    assert len(json_data) == 0
