import React, { useState, useEffect } from 'react';
import axios from 'axios';

function Recommendations({ contentId }) {
  const [recommendations, setRecommendations] = useState([]);

  useEffect(() => {
    axios.get(`http://localhost:8000/api/recommend/${contentId}/`)
      .then(response => {
        setRecommendations(response.data.recommended_content_ids);
      })
      .catch(error => console.error('Error fetching recommendations:', error));
  }, [contentId]);

  return (
    <div>
      <h2>Recommended Content</h2>
      <ul>
        {recommendations.map(id => (
          <li key={id}>Content ID: {id}</li>
        ))}
      </ul>
    </div>
  );
}

export default Recommendations;
