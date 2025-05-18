import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from adapters.persistence.models.model_job import Base, Job
from adapters.persistence.job_repository_impl import JobRepositoryImpl
from core.domain.job import JobCreate


@pytest.fixture
def session():
    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    sess = Session()
    yield sess
    sess.close()


def make_job_data(name="Job1"):
    return JobCreate(
        name_job=name,
        sequence_job="123",
        name_company="Empresa X",
        result_job="Sucesso",
        obs_job="Observação opcional",
        date=None,
    )


def test_create_job(session):
    repo = JobRepositoryImpl(session)
    job_data = JobCreate(
        name_job="Test Job",
        sequence_job="123",
        name_company="Empresa X",
        result_job="Sucesso",
        obs_job="Observação opcional",
    )
    job_response = repo.create_job(job_data)
    assert job_response.name_job == "Test Job"
    assert job_response.name_company == "Empresa X"
    assert session.query(Job).count() == 1


def test_get_jobs(session):
    repo = JobRepositoryImpl(session)
    job_data = JobCreate(
        name_job="Job1",
        sequence_job="123",
        name_company="Empresa ssssX",
        result_job="Sucesso",
        obs_job="Observação opcional",
    )
    job_data2 = JobCreate(
        name_job="Job2",
        sequence_job="123",
        name_company="Empresa ssssX",
        result_job="Sucesso",
        obs_job="Observação opcional",
    )
    repo.create_job(job_data)
    repo.create_job(job_data2)
    result = repo.get_jobs()
    assert isinstance(result, list)
    assert len(repo.get_jobs()) == 2
    assert result[0].name_job == "Job1"
    assert result[1].name_job == "Job2"


def test_get_job_by_id(session):
    repo = JobRepositoryImpl(session)
    job = repo.create_job(make_job_data("Job1"))
    found = repo.get_job_by_id(job.id_job)
    assert found is not None
    assert found.name_job == "Job1"
    assert repo.get_job_by_id(999) is None  # Não existe


def test_update_job(session):
    repo = JobRepositoryImpl(session)
    job = repo.create_job(make_job_data("Job1"))
    updated = repo.update_job(job.id_job, make_job_data("Updated"))
    assert updated.name_job == "Updated"
    assert session.query(Job).filter_by(id_job=job.id_job).first().name_job == "Updated"


def test_delete_job(session):
    repo = JobRepositoryImpl(session)
    job = repo.create_job(make_job_data("Job1"))
    repo.delete_job(job.id_job)
    assert session.query(Job).count() == 0
