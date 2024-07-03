from rest_framework import generics
from .models import Post
from .serializers import PostSerializer
from .serializers import UserSerializer
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets, permissions
from .models import Content
from .serializers import ContentSerializer
from algoliasearch_django import raw_search
from ml.load_model import load_recommendation_model, get_recommendations
from django.views.decorators.cache import cache_page
from .tasks import sample_task
from celery.result import AsyncResult

class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

@api_view(['POST'])
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(username=username, password=password)
    if user:
        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        })
    return Response({'error': 'Invalid credentials'}, status=401)

class SecureViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

class ContentViewSet(viewsets.ModelViewSet):
    queryset = Content.objects.all().order_by('-created_at')
    serializer_class = ContentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

@api_view(['GET'])
def search_content(request):
    query = request.GET.get('query', '')
    results = raw_search(Content, query)['hits']
    return Response(results)

@api_view(['GET'])
def recommend_content(request, content_id):
    cosine_sim, df, _ = load_recommendation_model()
    recommendations = get_recommendations(int(content_id), cosine_sim, df)
    return Response({'recommended_content_ids': recommendations})

@api_view(['GET'])
@cache_page(60 * 15)  # Cache the view for 15 minutes
def cached_view(request):
    return Response({"message": "This is a cached response"})

@api_view(['GET'])
def start_task(request):
    duration = request.GET.get('duration', 10)
    task = sample_task.delay(int(duration))
    return Response({'task_id': task.id})

@api_view(['GET'])
def check_task_status(request, task_id):
    task = AsyncResult(task_id)
    return Response({
        'task_id': task_id,
        'task_status': task.status,
        'task_result': task.result
    })