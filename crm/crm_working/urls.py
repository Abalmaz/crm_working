from django.urls import path
from crm_working import views

urlpatterns = [
    path('', views.index),
]