import Cookies from 'js-cookie';

import React, { useState } from 'react';

const CreateJob = () => {
  const [formData, setFormData] = useState({
    title: '',
    description: ''
    // Adicione mais campos do formulário conforme necessário
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
      const response = await fetch('http://127.0.0.1:8000/create/', {
        method: 'POST',
        headers: { 'X-CSRFToken': Cookies.get('csrftoken') },
        body: JSON.stringify(formData)
      });
      if (response.ok) {
        // Ação após a criação bem-sucedida do trabalho
      } else {
        // Tratamento de erros, se necessário
      }
    } catch (error) {
      // Tratamento de erros de conexão ou outras exceções
    }
  };

  return (
    <div>
      <h1>Create Job</h1>
      <form onSubmit={handleSubmit}>
        <label htmlFor="title">Title:</label>
        <input type="text" id="title" name="title" value={formData.title} onChange={handleChange} />
        <label htmlFor="description">Description:</label>
        <textarea id="description" name="description" value={formData.description} onChange={handleChange}></textarea>
        <button type="submit">Submit</button>
      </form>
    </div>
  );
};

export default CreateJob;
