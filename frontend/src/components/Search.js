import React, { useState } from 'react';
import algoliasearch from 'algoliasearch/lite';

const searchClient = algoliasearch('your_algolia_app_id', 'your_algolia_search_only_api_key');

function Search() {
  const [query, setQuery] = useState('');
  const [results, setResults] = useState([]);

  const handleSearch = async (e) => {
    e.preventDefault();
    const { hits } = await searchClient
      .initIndex('content')
      .search(query);
    setResults(hits);
  };

  return (
    <div>
      <form onSubmit={handleSearch}>
        <input 
          type="text" 
          value={query} 
          onChange={(e) => setQuery(e.target.value)} 
          placeholder="Search..."
        />
        <button type="submit">Search</button>
      </form>
      <ul>
        {results.map((item) => (
          <li key={item.objectID}>{item.title}</li>
        ))}
      </ul>
    </div>
  );
}

export default Search;
