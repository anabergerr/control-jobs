from core.domain.job import JobCreate, JobResponse


def test_job_create_valid():
    job = JobCreate(
        name_job="Dev",
        sequence_job="001",
        name_company="Empresa",
        result_job="Aprovado",
    )
    assert job.name_job == "Dev"


def test_job_response_optional_fields():
    job = JobResponse(
        id_job=1,
        name_job="Dev",
        sequence_job="001",
        name_company="Empresa",
        result_job="Aprovado",
    )
    assert job.obs_job is None
    assert job.date is None
