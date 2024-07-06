from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('user_add', views.user_add, name='user_add'),
    path("about", views.about_page, name="about"),
    path("templates", views.templates, name="templates"),
    path("carrito", views.carrito, name="carrito"),
    path("panel", views.panel, name="panel"),
    path("template_add", views.template_add, name="template_add"),
    path("add_template", views.add_template, name="add_template"),
    path("remove_template/<int:pk>/", views.remove_template, name="remove_template"),

    path('register', views.register, name='register'),
    
    path('login', views.conectar, name="login"),
    path("logout", views.desconectar, name="logout"),
]