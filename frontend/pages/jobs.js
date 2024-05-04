import { useState, useEffect } from 'react';
import axios from 'axios';

const ListJobs = () => {
  const [jobs, setJobs] = useState([]);
  const [filteredJobs, setFilteredJobs] = useState([]);
  const [searchInput, setSearchInput] = useState('');
  const [dateInput, setDateInput] = useState('');
  const [companyInput, setCompanyInput] = useState('');

  useEffect(() => {
    // Fetch para buscar os trabalhos da API
    axios.get('http://127.0.0.1:8000/jobs/')
      .then(response => {
        setJobs(response.data);
        setFilteredJobs(response.data); // Definir os trabalhos filtrados inicialmente como todos os trabalhos
      })
      .catch(error => console.error('Erro ao buscar trabalhos:', error));
  }, []); // Executar uma vez, quando o componente montar

  const handleSearchInputChange = (event) => {
    setSearchInput(event.target.value.toUpperCase());
  };

  const handleDateInputChange = (event) => {
    setDateInput(event.target.value);
  };

  const handleCompanyInputChange = (event) => {
    setCompanyInput(event.target.value);
  };

  const filterTable = () => {
    const filteredJobs = jobs.filter(job => {
      const titleMatch = job.title.toUpperCase().includes(searchInput);
      const dateMatch = !dateInput || new Date(job.date).toISOString().split('T')[0] === dateInput;

      let companyMatch = true;
      if (companyInput === 'Yes' || companyInput === 'No') {
        companyMatch = job.company_return === companyInput;
      } else if (companyInput === 'All') {
        companyMatch = true;
      }

      return titleMatch && dateMatch && companyMatch;
    });
    setFilteredJobs(filteredJobs);
  };

  useEffect(() => {
    filterTable();
  }, [searchInput, dateInput, companyInput]);

  const handleDeleteJob = (id) => {
    if (window.confirm('Tem certeza que deseja excluir este trabalho?')) {
      axios.delete(`http://127.0.0.1:8000/delete/${id}`)
        .then(response => {
          if (response.status === 200) {
            // Se a exclusão for bem-sucedida, atualize a lista de trabalhos
            setJobs(jobs.filter(job => job.id !== id));
            setFilteredJobs(filteredJobs.filter(job => job.id !== id));
          } else {
            console.error('Erro ao excluir o trabalho');
          }
        })
        .catch(error => console.error('Erro ao excluir o trabalho:', error));
    }
  };

  return (
    <div>
      <h1>List Jobs</h1>
      <div className="filters">
        <input
          type="text"
          id="search-input"
          placeholder="Search for job title"
          value={searchInput}
          onChange={handleSearchInputChange}
        />
        <input
          type="date"
          id="date-input"
          value={dateInput}
          onChange={handleDateInputChange}
        />
        <select
          id="company-input"
          value={companyInput}
          onChange={handleCompanyInputChange}
        >
          <option value="">All</option>
          <option value="Yes">Yes</option>
          <option value="No">No</option>
        </select>
      </div>

      <table id="job-table">
        <thead>
          <tr>
            <th>Title</th>
            <th>Date</th>
            <th>Type</th>
            <th>Company Response</th>
            <th>Action</th>
          </tr>
        </thead>
        <tbody>
          {filteredJobs.map((job) => (
            <tr
              key={job.id}
              style={{ cursor: 'pointer' }}
            >
              <td>{job.title}</td>
              <td>{job.date}</td>
              <td>{job.type_job}</td>
              <td>{job.company_return}</td>
              <td>
                <button className="delete-btn" onClick={() => handleDeleteJob(job.id)}>deleti</button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
      <a href="/create">
        <button className="create-job">Add Job</button>
      </a>
    </div>
  );
};

export default ListJobs;
