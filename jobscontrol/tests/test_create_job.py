import pytest
from app import create_app, db
from app.models import Job
from flask import json


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

def test_create_job(client):
    # Define o payload (dados) para a requisição POST
    payload = {
        "name_job": "Desenvolvedor Backend",
        "sequence_job": "12345",
        "name_company": "Tech Solutions",
        "result_job": "Projeto concluído com sucesso",
        "obs_job": "Trabalho remoto, entregas semanais",
        "date": "2023-10-05T14:30:00"
    }

    # Faz uma requisição POST para a rota /create
    response = client.post('/create', data=json.dumps(payload), content_type='application/json')

    # Verifica se a resposta tem o status code 201 (Created)
    assert response.status_code == 201

    # Verifica se a mensagem de sucesso está presente na resposta
    data = json.loads(response.data)
    assert data['message'] == 'Job created successfully!'

    # Verifica se o Job foi realmente criado no banco de dados
    job = Job.query.filter_by(name_job="Desenvolvedor Backend").first()
    assert job is not None
    assert job.sequence_job == "12345"
    assert job.name_company == "Tech Solutions"
    assert job.result_job == "Projeto concluído com sucesso"
    assert job.obs_job == "Trabalho remoto, entregas semanais"