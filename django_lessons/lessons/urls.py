from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register, name= 'register'),
    path('index1', views.index1, name= 'index1')
    # path('register', views.register, name='register'),
    # path('login', views.login, name='login'),
    # path('logout', views.logout, name='logout'),
]