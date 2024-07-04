from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register, name='register'),
    path('user_add', views.user_add, name='user_add'),
    path('login', views.conectar, name="login"),
    path("logout", views.desconectar, name="logout"),
]