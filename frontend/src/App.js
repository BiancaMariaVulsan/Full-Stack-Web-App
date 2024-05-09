import React, { useState } from 'react';
import axios from 'axios';
import { BrowserRouter as Router, Route, Redirect } from 'react-router-dom';

function App() {
  const [auth, setAuth] = useState(false);
  const [token, setToken] = useState('');

  const login = (username, password) => {
    axios.post('http://localhost:8000/token/', { username, password })
      .then(response => {
        setToken(response.data.access);
        setAuth(true);
      })
      .catch(error => console.error('Error logging in:', error));
  };

  return (
    <Router>
      <Route exact path="/">
        {auth ? <h1>Welcome</h1> : <Redirect to="/login" />}
      </Route>
      <Route path="/login">
        <LoginForm login={login} />
      </Route>
    </Router>
  );
}

function LoginForm({ login }) {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    login(username, password);
  };

  return (
    <form onSubmit={handleSubmit}>
      <input
        type="text"
        value={username}
        onChange={(e) => setUsername(e.target.value)}
        placeholder="Username"
      />
      <input
        type="password"
        value={password}
        onChange={(e) => setPassword(e.target.value)}
        placeholder="Password"
      />
      <button type="submit">Login</button>
    </form>
  );
}

export default App;