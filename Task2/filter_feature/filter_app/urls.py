from django.urls import path
from . import views

urlpatterns = [
    path('', views.filter_boxes, name='filter_boxes'),
]
