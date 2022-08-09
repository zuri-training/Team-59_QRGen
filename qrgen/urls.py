from django.urls import path
from .views import *

urlpatterns = [
    path('dashboard/', dashboard, name='dashboard'),
    path('dashboard_website/', dashboard_website, name='dashboard_website'),
    path('dashboard_website_2/', dashboard_website_2, name='dashboard_website_2'),
    path('dashboard_email/', dashboard_email, name='dashboard_email'),
    path('dashboard_email_2/', dashboard_email_2, name='dashboard_email_2'),
    path('dashboard_text/', dashboard_text, name='dashboard_text'),
    path('dashboard_text_2/', dashboard_text_2, name='dashboard_text_2'),
    path('dashboard_whatsapp/', dashboard_whatsapp, name='dashboard_whatsapp'),
    path('dashboard_whatsapp_2/', dashboard_whatsapp_2, name='dashboard_whatsapp_2'),

    # For data stored on dashboard

    path('', QrListView.as_view(), name='list'),
    path('qrgen/<int:pk>/', QrDetailView.as_view(), name='detail'),
    path('qrgen/<int:pk>/update/', QrUpdateView.as_view(), name='update'),
    path('qrcode/<int:pk>/delete/', QrDeleteView.as_view(), name='delete'),
]
