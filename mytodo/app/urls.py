from django.urls import path
from app import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('ticket/<int:pk>/', views.TicketDetailView.as_view(), name='ticket_detail'),
]
