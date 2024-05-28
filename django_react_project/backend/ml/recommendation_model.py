import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
import pickle

# Sample data: Assuming you have a dataset with content IDs and their respective descriptions
data = {
    'content_id': [1, 2, 3, 4, 5],
    'description': [
        'Django React project tutorial',
        'Machine learning basics',
        'Introduction to Python',
        'Deep learning with TensorFlow',
        'Scikit-learn for data analysis'
    ]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Create a TF-IDF Vectorizer to convert descriptions to vectors
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(df['description'])

# Calculate the cosine similarity between the vectors
cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

# Save the model (cosine similarity matrix and tfidf) to disk
with open('recommendation_model.pkl', 'wb') as f:
    pickle.dump((cosine_sim, df, tfidf), f)
