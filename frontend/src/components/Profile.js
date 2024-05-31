import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { useHistory } from 'react-router-dom';

const Profile = () => {
    const userContentId = 1;  // Example content ID for testing
    const [user, setUser] = useState(null);
    const history = useHistory();

    useEffect(() => {
        const fetchUser = async () => {
            try {
                const accessToken = localStorage.getItem('access');
                const response = await axios.get('http://localhost:8000/api/profile/', {
                    headers: {
                        Authorization: `Bearer ${accessToken}`
                    }
                });
                setUser(response.data);
            } catch (error) {
                console.error('Failed to fetch user:', error);
                history.push('/login'); // Redirect to login if failed
            }
        };

        fetchUser();
    }, [history]);

    return (
        <div>
            <h1>User Profile</h1>
            {user ? (
                <div>
                    <h1>User Profile</h1>
                    <p><strong>Username:</strong> {user.username}</p>
                    <Recommendations contentId={userContentId} />
                </div>
            ) : (
                <p>Loading...</p>
            )}
        </div>
    );
};

export default Profile;
