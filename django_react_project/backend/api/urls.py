from django.urls import path
from .views import ContentViewSet, PostList, PostDetail, SecureViewSet, UserViewSet, login
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import search_content
from .views import recommend_content

urlpatterns = [
    path('posts/', PostList.as_view(), name='post-list'),
    path('posts/<int:pk>/', PostDetail.as_view(), name='post-detail'),
    path('login/', login),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('search/', search_content, name='search_content'),
    path('recommend/<int:content_id>/', recommend_content, name='recommend_content'),
]

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'secure-users', SecureViewSet, basename='secure-user')
router.register(r'contents', ContentViewSet, basename='content')

urlpatterns = router.urls