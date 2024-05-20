import axios from 'axios';

export const fetchContents = () => {
    return async (dispatch) => {
        dispatch({ type: 'FETCH_CONTENTS_REQUEST' });
        try {
            const response = await axios.get('http://localhost:8000/api/contents/');
            dispatch({ type: 'FETCH_CONTENTS_SUCCESS', payload: response.data });
        } catch (error) {
            dispatch({ type: 'FETCH_CONTENTS_FAILURE', payload: error.message });
        }
    };
};
