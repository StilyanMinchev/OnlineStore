from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('<int:pk>/', views.watch_details, name="watch details"),
    # path('<int:pk>/<str:slug>/', views.watch_details, name="watch details"),
    path('create/', views.create, name="create"),
    path('delete/<int:pk>/', views.delete_watch, name='delete watch'),
    path('edit/<int:pk>/', views.edit_watch, name='edit watch'),
    path('like/<int:pk>/', views.like_watch, name='like watch'),
]
