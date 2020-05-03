from django.urls import path
from signapp import views
from django.shortcuts import redirect

urlpatterns = [
    path('logout/', views.logout_view, name='logout'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('', lambda request: redirect('profile_edit/', permanent=True)),

] 