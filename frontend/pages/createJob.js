import React, { useState } from 'react';
import axios from 'axios'; // Importar o Axios
import Cookies from 'js-cookie';
import styles from '../styles/CreateJob.module.css';

const CreateJob = () => {
  const [formData, setFormData] = useState({
    title: '',
    type_job: '',
    company_return: 'No', // Definindo o valor padrão para 'No'
    date: ''
  });
  const [darkMode, setDarkMode] = useState(false);

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      console.log('SSSSSS', formData)
      const csrftoken = Cookies.get('csrftoken');
      const response = await axios.post('http://127.0.0.1:8000/create/', formData, {
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

  const toggleDarkMode = () => {
    setDarkMode(!darkMode);
  };

  return (
    <div className={`${styles.container} ${darkMode ? styles.dark : ''}`}>
      <h1 className={styles.heading}>Create Job</h1>
      <button onClick={toggleDarkMode} className={styles.darkModeButton}>
        {darkMode ? 'Switch to Light Mode' : 'Switch to Dark Mode'}
      </button>
      <form className={styles.form} onSubmit={handleSubmit}>
        <label htmlFor="title" className={styles.label}>Title:</label>
        <input type="text" id="title" name="title" value={formData.title} onChange={handleChange} className={styles.input} />

        <label htmlFor="type_job" className={styles.label}>Type of Job:</label>
        <input type="text" id="type_job" name="type_job" value={formData.type_job} onChange={handleChange} className={styles.input} />

        <label htmlFor="company_return" className={styles.label}>Company Return:</label>
        <select id="company_return" name="company_return" value={formData.company_return} onChange={handleChange} className={styles.select}>
          <option value="Yes">Yes</option>
          <option value="No">No</option>
        </select>

        <label htmlFor="date" className={styles.label}>Date:</label>
        <input type="date" id="date" name="date" value={formData.date} onChange={handleChange} className={styles.input} />

        <button type="submit" className={styles.button}>Submit</button>
      </form>
    </div>
  );
};

export default CreateJob;
