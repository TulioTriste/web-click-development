from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register, name='register'),
    path('user_add', views.user_add, name='user_add'),

    path('accounts/', include('django.contrib.auth.urls'))
]