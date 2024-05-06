from django.urls import path
from .views import PostList, PostDetail
from rest_framework.routers import DefaultRouter
from .views import UserViewSet

urlpatterns = [
    path('posts/', PostList.as_view(), name='post-list'),
    path('posts/<int:pk>/', PostDetail.as_view(), name='post-detail'),
]

router = DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = router.urls