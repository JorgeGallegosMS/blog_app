from django.contrib.auth import views as login_views
from django.urls import path
from . import views


urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', login_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', login_views.LogoutView.as_view(template_name='users/logout.html'), name='logout')
]