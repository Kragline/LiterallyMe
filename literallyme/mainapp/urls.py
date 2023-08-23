from django.urls import path
from .views import *


urlpatterns = [
    # Movie
    path('', MovieListView.as_view(), name='home'),
    path('add_movie/', AddMovieView.as_view(), name='add_movie'),
    path('movie/<slug:movie_slug>/', about_movie_view, name='about_movie'),
    path('movie/<slug:movie_slug>/update/', UpdateMovieView.as_view(), name='update_movie'),
    path('movie/<slug:movie_slug>/delete/', DeleteMovieView.as_view(), name='delete_movie'),

    # Actor
    path('actors/', ActorsListView.as_view(), name='actors'),
    path('add_actor/', AddActorView.as_view(), name='add_actor'),
    path('actor/<slug:actor_slug>/', AboutActorView.as_view(), name='about_actor'),
    path('actor/<slug:actor_slug>/update/', UpdateActorView.as_view(), name='update_actor'),
    path('actor/<slug:actor_slug>/delete/', DeleteActorView.as_view(), name='delete_actor'),

    # Category
    path('movie/categories/<slug:category_slug>/', CategoryListView.as_view(), name='category'),
    path('add_category/', AddCategoryView.as_view(), name='add_category'),

    # Comment
    path('movie/<slug:movie_slug>/comment/update/<int:comment_id>/', UpdateCommentView.as_view(), name='update_comment'),
    path('movie/<slug:movie_slug>/comment/delete/<int:comment_id>/', DeleteCommentView.as_view(), name='delete_comment'),

    # search views
    path('search-movie', search_for_movies_view, name='movie_search'),
    path('search-actor', search_for_actors_view, name='actor_search'),
]
