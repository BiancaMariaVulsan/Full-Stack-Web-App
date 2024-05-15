from django.urls import path
from .views import PostList, PostDetail, SecureViewSet
from rest_framework.routers import DefaultRouter
from .views import UserViewSet
from .views import login
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('posts/', PostList.as_view(), name='post-list'),
    path('posts/<int:pk>/', PostDetail.as_view(), name='post-detail'),
    path('login/', login),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'secure-users', SecureViewSet, basename='secure-user')

urlpatterns = router.urls