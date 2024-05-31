from django.test import TestCase
from django.urls import reverse

class RecommendationApiTest(TestCase):

    def test_recommendation_api(self):
        response = self.client.get(reverse('recommend_content', args=[1]))
        self.assertEqual(response.status_code, 200)
        self.assertIn('recommended_content_ids', response.json())
