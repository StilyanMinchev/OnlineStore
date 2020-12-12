from django.urls import path, include

from store_auth.views import login_user, register_user, user_profile, LogOutView

urlpatterns = (
    path('register/', register_user, name='register user'),
    path('login/', login_user, name='login user'),
    path('logout/', LogOutView.as_view(), name='logout user'),
    path('', include('django.contrib.auth.urls')),
    path('profile/', user_profile, name='current user profile'),
    path('profile/<int:pk>/', user_profile, name='user profile'),
)
