from .views import HelloWorld
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('hello/', HelloWorld.as_view(), name='hello_world'),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
]