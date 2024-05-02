from django.urls import path, include
from django.contrib import admin
from .views import PostList, PostDetail

urlpatterns = [
    path('posts/', PostList.as_view(), name='post_list'),
    path('posts/<int:pk>/', PostDetail.as_view(), name='post_detail'),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
]