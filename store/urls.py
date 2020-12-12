from django.urls import path
from . import views
from .views import CommentWatchView, WatchDetailsView, LikeWatchView

urlpatterns = [
    path('', views.index, name="index"),
    # path('<int:pk>/', views.watch_details, name="watch details"),
    path('<int:pk>/', WatchDetailsView.as_view(), name="watch details"),
    path('create/', views.create, name="create"),
    path('delete/<int:pk>/', views.delete_watch, name='delete watch'),
    path('edit/<int:pk>/', views.edit_watch, name='edit watch'),
    path('like/<int:pk>/', LikeWatchView.as_view(), name='like watch'),
    path('comment/<int:pk>/', CommentWatchView.as_view(), name='comment watch'),
]
