from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='posts-index'),
    path('details/<id>/', views.details, name='posts-details')
]