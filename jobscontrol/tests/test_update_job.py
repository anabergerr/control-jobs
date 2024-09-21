from datetime import datetime

import pytest
from flask import json

from app import create_app, db
from app.models import Job


@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    with app.app_context():
        db.create_all()
        # Cria um job de exemplo para os testes
        job = Job(
            name_job='Desenvolvedor Backend',
            sequence_job='12345',
            name_company='Tech Solutions',
            result_job='Projeto concluído com sucesso',
            obs_job='Trabalho remoto, entregas semanais',
            date=datetime(2023, 10, 5, 14, 30),
        )
        db.session.add(job)
        db.session.commit()

        yield app.test_client()

        db.drop_all()


def test_update_job_partial_success(client):
    # Define o payload para a requisição PATCH
    payload = {
        'name_job': 'Desenvolvedor Frontend',
        'sequence_job': '54321',
        'name_company': 'Tech Innovations',
        'result_job': 'Projeto em andamento',
        'obs_job': 'Trabalho presencial',
        'date': '2023-11-01T10:00:00',
    }
    # Faz uma requisição PATCH para atualizar o job com id 1
    response = client.patch(
        '/jobs/1', data=json.dumps(payload), content_type='application/json'
    )

    # Verifica se a resposta tem o status code 200 (OK)
    status_update = 200
    assert response.status_code == status_update

    # Verifica se a mensagem de sucesso está presente na resposta
    data = json.loads(response.data)
    assert data['message'] == 'Job updated partially!'

    # Verifica se o job foi atualizado corretamente no banco de dados
    job = db.session.get(Job, 1)  # Alterado para Session.get()
    assert job.name_job == 'Desenvolvedor Frontend'
    assert job.sequence_job == '54321'
    assert job.name_company == 'Tech Innovations'
    assert job.result_job == 'Projeto em andamento'
    assert job.obs_job == 'Trabalho presencial'
    assert job.date == datetime(2023, 11, 1, 10, 0)
