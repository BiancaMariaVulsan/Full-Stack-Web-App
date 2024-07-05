from django.test import TestCase
from django.urls import reverse
from django.core.cache import cache
import time

class RecommendationApiTest(TestCase):

    def test_recommendation_api(self):
        response = self.client.get(reverse('recommend_content', args=[1]))
        self.assertEqual(response.status_code, 200)
        self.assertIn('recommended_content_ids', response.json())

class RedisTests(TestCase):
    def setUp(self):
        self.client = self.client

    def test_cache_view(self):
        url = reverse('cached_view')
        
        # Initial request should miss the cache
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertIn("This is a cached response", response.content.decode())

        # Wait a short period and make the request again
        time.sleep(1)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertIn("This is a cached response", response.content.decode())

    def test_cache_expiry(self):
        url = reverse('cached_view')
        
        # Set a cache value manually
        cache.set('cached_view_key', 'This is a cached response', timeout=1)
        
        # Fetch the cached value
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertIn("This is a cached response", response.content.decode())
        
        # Wait for cache to expire
        time.sleep(2)
        
        # Try fetching the value again; it should not be present
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertNotIn("This is a cached response", response.content.decode())