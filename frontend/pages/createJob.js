import React, { useState } from 'react';
import axios from 'axios'; // Importar o Axios
import Cookies from 'js-cookie';

const CreateJob = () => {
  const [formData, setFormData] = useState({
    title: '',
    type_job: '',
    company_return: 'No', // Definindo o valor padrão para 'No'
    date: ''
  });

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const formDataToSend = new FormData();
      formDataToSend.append('title', formData.title);
      formDataToSend.append('type_job', formData.type_job);
      formDataToSend.append('company_return', formData.company_return);
      formDataToSend.append('date', formData.date);

      console.log(typeof formData);

      const csrftoken = Cookies.get('csrftoken');
      const response = await axios.post('http://127.0.0.1:8000/create/', formDataToSend, {
        withCredentials: true,
        headers: {
          'X-CSRFToken': csrftoken
        }
      });
      if (response.status === 200) {
        console.log('Job created successfully');
      } else {
        console.log('Error creating job');
      }
    } catch (error) {
      console.error('Error:', error);
    }
  };


  return (
    <div>
      <h1>Create Job</h1>
      <form onSubmit={handleSubmit}>
        <label htmlFor="title">Title:</label>
        <input type="text" id="title" name="title" value={formData.title} onChange={handleChange} />

        <label htmlFor="type_job">Type of Job:</label>
        <input type="text" id="type_job" name="type_job" value={formData.type_job} onChange={handleChange} />

        <label htmlFor="company_return">Company Return:</label>
        <select id="company_return" name="company_return" value={formData.company_return} onChange={handleChange}>
          <option value="Yes">Yes</option>
          <option value="No">No</option>
        </select>

        <label htmlFor="date">Date:</label>
        <input type="date" id="date" name="date" value={formData.date} onChange={handleChange} />

        <button type="submit">Submit</button>
      </form>
    </div>
  );
};

export default CreateJob;
