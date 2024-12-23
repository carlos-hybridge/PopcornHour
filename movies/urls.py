from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.user_login, name='user_login'),
    path('register/', views.user_register, name='user_register'),
    path('reviews/<int:movie_id>/comment/', views.add_comment, name='add_comment'),
]
