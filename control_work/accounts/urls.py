from django.urls import path
from django.contrib.auth import views as django_views

from accounts import views

urlpatterns = [

    path('login', django_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout', django_views.LogoutView.as_view(), name='logout'),
    path('register', views.RegisterView.as_view(), name='register'),
    path('profile/<int:id>', views.UserDetailView.as_view(), name='profile'),
    path('profile/update', views.UserUpdateView.as_view(), name='profile_update'),
    path('profile/<int:id>/change-password', views.UserPasswordChangeView.as_view(), name='user_change_password')

]