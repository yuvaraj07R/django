from django.urls import path
from . import views

urlpatterns = [
    path('yuvi/', views.yuvi, name='yuvi'),
]