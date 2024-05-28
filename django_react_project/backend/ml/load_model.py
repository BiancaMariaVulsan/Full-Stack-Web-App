import pickle

def load_recommendation_model():
    with open('backend/ml/recommendation_model.pkl', 'rb') as f:
        cosine_sim, df, tfidf = pickle.load(f)
    return cosine_sim, df, tfidf

def get_recommendations(content_id, cosine_sim, df):
    idx = df.index[df['content_id'] == content_id][0]

    sim_scores = list(enumerate(cosine_sim[idx]))

    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    sim_scores = sim_scores[1:6]

    content_indices = [i[0] for i in sim_scores]

    return df['content_id'].iloc[content_indices].tolist()
