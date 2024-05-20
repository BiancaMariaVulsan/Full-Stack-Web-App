import React, { useEffect } from 'react';
import axios from 'axios';
import { BrowserRouter as Router, Route, Redirect, Switch } from 'react-router-dom';
import { useDispatch, useSelector } from 'react-redux';
import { fetchContents } from './redux/actions/contentActions';
import Login from './components/Login';
import Profile from './components/Profile';

function App() {
  const [auth, setAuth] = useState(false);
  const [token, setToken] = useState('');
  const dispatch = useDispatch();
  
  const contents = useSelector(state => state.content.contents);
  const loading = useSelector(state => state.content.loading);
  const error = useSelector(state => state.content.error);

  const login = (username, password) => {
    axios.post('http://localhost:8000/api/login/', { username, password })
      .then(response => {
        setToken(response.data.access);
        setAuth(true);
        dispatch(fetchContents());  // Fetch content immediately after login
      })
      .catch(error => console.error('Error logging in:', error));
  };

  const handleLogout = () => {
    setToken('');
    setAuth(false);
  };

  useEffect(() => {
    if (auth) {
      dispatch(fetchContents());
    }
  }, [auth, dispatch]);

  return (
    <Router>
      <Switch>
        <Route exact path="/">
          {auth ? <Redirect to="/profile" /> : <Redirect to="/login" />}
        </Route>
        <Route path="/login">
          {auth ? <Redirect to="/profile" /> : <Login login={login} />}
        </Route>
        <Route path="/profile">
          {auth ? (
            <Profile 
              token={token} 
              setAuth={setAuth}
              contents={contents}
              loading={loading}
              error={error}
            />
          ) : (
            <Redirect to="/login" />
          )}
        </Route>
        <Route path="/logout">
          {handleLogout()}
          <Redirect to="/login" />
        </Route>
      </Switch>
    </Router>
  );
}

export default App;
