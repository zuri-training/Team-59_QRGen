from django.urls import path
from .views import GenerationDashboardView, MainDashboardView, DeleteQrCode, EditQrCode, download
from . import views
app_name = 'qrgen'

urlpatterns = [
    path('generate/', GenerationDashboardView.as_view(), name='generate'),
    path('', MainDashboardView.as_view(), name='dashboard'),
    path('delete/<int:code_id>/', DeleteQrCode.as_view(), name='delete_qrcode'),
    path('edit/<int:code_id>/', EditQrCode.as_view(), name='edit_qrcode'),
    path('download/<int:code_id>/<str:type>/', download, name='download_qrcode'),    
]
