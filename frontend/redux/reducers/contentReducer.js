const initialState = {
    contents: [],
    loading: false,
    error: null,
};

export default function contentReducer(state = initialState, action) {
    switch (action.type) {
        case 'FETCH_CONTENTS_REQUEST':
            return {
                ...state,
                loading: true,
                error: null,
            };
        case 'FETCH_CONTENTS_SUCCESS':
            return {
                ...state,
                loading: false,
                contents: action.payload,
            };
        case 'FETCH_CONTENTS_FAILURE':
            return {
                ...state,
                loading: false,
                error: action.payload,
            };
        default:
            return state;
    }
}
