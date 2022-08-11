from django.urls import path
from .views import GenerationDashboardView, MainDashboardView
from . import views

app_name = 'qrgen'

urlpatterns = [
    path('generate/', GenerationDashboardView.as_view(), name='generate'),
    path('', MainDashboardView.as_view(), name='dashboard'),
]
