from django.urls import path
from studentapp import views


urlpatterns = [
    path('user/<slug:slug>', views.details_view, name='details'),
    path('home/', views.home, name = 'home'),
    path('profile_edit/', views.profile_edit, name='profile_edit'),    

] 