from django.urls import path

from .views import home, download

urlpatterns = [
    path('<int:pk>/', home, name='home'),
    path('download/<int:pk>/', download, name='download'),
]