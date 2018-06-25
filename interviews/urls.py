from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('interviews/', views.interviews, name='interviews'),
    path('test', views.baa)
]