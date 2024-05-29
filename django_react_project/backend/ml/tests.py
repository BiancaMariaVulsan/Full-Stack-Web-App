import unittest
from .load_model import load_recommendation_model, get_recommendations

class TestRecommendationModel(unittest.TestCase):

    def setUp(self):
        self.cosine_sim, self.df, self.tfidf = load_recommendation_model()

    def test_recommendation(self):
        recommendations = get_recommendations(1, self.cosine_sim, self.df)
        self.assertEqual(len(recommendations), 5)
        self.assertIn(2, recommendations)

if __name__ == '__main__':
    unittest.main()
