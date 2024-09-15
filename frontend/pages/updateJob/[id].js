import { useState, useEffect } from 'react';
import { useRouter } from 'next/router';
import axios from 'axios';

const UpdateJob = () => {
  const [formData, setFormData] = useState({});
  const router = useRouter();
  const { slug } = router.query; // Alterando de 'id' para 'slug'

  useEffect(() => {
    console.log("ENTREI AQUI NESTE CARALHO");
    const fetchJob = async () => {
      try {
        const response = await axios.get(`http://127.0.0.1:8000/jobs/${slug}`); // Alterando de 'id' para 'slug'
        setFormData(response.data);
        console.log('DADOSSSS', response.data);
      } catch (error) {
        console.error('Erro ao buscar job:', error);
      }
    };

    if (slug) { // Alterando de 'id' para 'slug'
      fetchJob();
    }
  }, [slug]); // Alterando de 'id' para 'slug'

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData(prevState => ({
      ...prevState,
      [name]: value
    }));
    console.log(name, value);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post(`/updateJob/${slug}`, formData); // Alterando de 'id' para 'slug'
      if (response.status === 200) {
        alert('Job updated successfully');
        router.push('/jobs');
      } else {
        throw new Error('Failed to update job');
      }
    } catch (error) {
      console.error('Erro ao atualizar job:', error);
    }
  };

  return (
    <div>
      <h1>Update Job</h1>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          name="title"
          placeholder="Title"
          value={formData.title || ''}
          onChange={handleChange}
        />
        <input
          type="text"
          name="type_job"
          placeholder="Type"
          value={formData.type_job || ''}
          onChange={handleChange}
        />
        <input
          type="text"
          name="company_return"
          placeholder="Company Response"
          value={formData.company_return || ''}
          onChange={handleChange}
        />
        <input
          type="date"
          name="date"
          value={formData.date || ''}
          onChange={handleChange}
        />
        <button type="submit">Update Job</button>
      </form>
    </div>
  );
};

export default UpdateJob;
