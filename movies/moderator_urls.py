from django.urls import path
from . import views

urlpatterns = [
    # URL de login para moderadores
    path('login/', views.moderator_login, name='moderator_login'),

    # URL para registrar un nuevo moderador
    path('register/', views.moderator_register, name='moderator_register'),

    # URL para el dashboard del moderador
    path('dashboard/', views.moderator_dashboard, name='moderator_dashboard'),

    # URL para agregar una nueva película (CRUD para moderadores)
    path('add/', views.add_movie, name='add_movie'),

    # URL para editar una película
    path('edit/<int:movie_id>/', views.edit_movie, name='edit_movie'),

    # URL para eliminar una película
    path('delete/<int:movie_id>/', views.delete_movie, name='delete_movie'),

    path('restore/<int:movie_id>/', views.restore_movie, name='restore_movie')
]
