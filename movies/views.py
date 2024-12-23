from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseForbidden
from .models import Movie, Comment, Rating
from users.models import RoleUser
from .forms import (
    LoginForm,
    UserRegisterForm,
    ModeratorRegisterForm,
    MovieRegisterForm,
    CommentForm,
)


# Home para mostrar películas
def home(request):
    movies = Movie.objects.filter(deleted_at__isnull=True)
    for movie in movies:
        comments = Comment.objects.filter(movie_id=movie.id, deleted_at__isnull=True).select_related('user')
        movie.comments = [{'text': comment.text, 'username': comment.user.username} for comment in comments]

    return render(request, 'movies/home.html', {'movies': movies})


# Login de usuarios estándar
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user and not user.is_staff:
                login(request, user)
                return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'movies/user_login.html', {'form': form})


# Login de moderadores
def moderator_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user and user.is_staff:
                login(request, user)
                return redirect('moderator_dashboard')
    else:
        form = LoginForm()
    return render(request, 'movies/moderator_login.html', {'form': form})


# Registro de usuarios estándar
def user_register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('user_login')
    else:
        form = UserRegisterForm()
    return render(request, 'movies/user_register.html', {'form': form})


# Registro de moderadores
def moderator_register(request):
    if request.method == 'POST':
        form = ModeratorRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_staff = True
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('moderator_login')
    else:
        form = ModeratorRegisterForm()
    return render(request, 'movies/moderator_register.html', {'form': form})


# CRUD de películas para moderadores
@login_required
def moderator_dashboard(request):
    if not request.user.is_staff:
        return HttpResponseForbidden()
    movies = Movie.objects.all()
    return render(request, 'movies/moderator_dashboard.html', {'movies': movies})


@login_required
def add_movie(request):
    if not request.user.is_staff:
        return HttpResponseForbidden()
    if request.method == 'POST':
        form = MovieRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('moderator_dashboard')
    else:
        form = MovieRegisterForm()
    return render(request, 'movies/add_movie.html', {'form': form})


@login_required
def edit_movie(request, movie_id):
    if not request.user.is_staff:
        return HttpResponseForbidden()
    movie = get_object_or_404(Movie, pk=movie_id)
    if request.method == 'POST':
        form = MovieRegisterForm(request.POST, request.FILES, instance=movie)
        if form.is_valid():
            form.save()
            return redirect('moderator_dashboard')
    else:
        form = MovieRegisterForm(instance=movie)
    return render(request, 'movies/edit_movie.html', {'form': form})


@login_required
def delete_movie(request, movie_id):
    if not request.user.is_staff:
        return HttpResponseForbidden()
    movie = get_object_or_404(Movie, pk=movie_id)
    # movie.deleted_at = timezone.now()
    movie.save()
    return redirect('moderator_dashboard')


# Comentarios
@login_required
def add_comment(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.movie = movie
            comment.user = request.user
            comment.save()
            return redirect('home')
    else:
        form = CommentForm()
    return render(request, 'movies/add_comment.html', {'form': form, 'movie': movie})
