from django.urls import path
from .views import dynamic_code_scan, download

app_name = 'handlescan'

urlpatterns = [
    path('dynamic/<int:code_id>/', dynamic_code_scan, name='dynamic'),
    path('download/<int:file_id>/', download, name='download'),
]
