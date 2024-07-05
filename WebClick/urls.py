from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('user_add', views.user_add, name='user_add'),
    path("about", views.about_page, name="about"),
    path("templates", views.templates, name="templates"),
    path("carrito", views.carrito, name="carrito"),

    path('register', views.register, name='register'),
    
    path('login', views.conectar, name="login"),
    path("logout", views.desconectar, name="logout"),
]