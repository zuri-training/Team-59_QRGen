from django.urls import path
from .views import GenerationDashboardView, MainDashboardView

app_name = 'qrgen2'

urlpatterns = [
    path('generate', GenerationDashboardView.as_view(), name='generate'),
    path('', MainDashboardView.as_view(), name='dashboard'),
]
