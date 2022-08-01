from django.urls import path

from .views import home, dashboard, download

urlpatterns = [
    path('', home, name='home'),
    path('dashboard/<int:pk>/', dashboard, name='dashboard'),
    path('download/<int:pk>/', download, name='download'),
]