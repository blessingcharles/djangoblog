from django.urls import path
from . import views 
from django.contrib.auth import views as auth_views

app_name='Authentication'

urlpatterns = [
    path('register/',views.register,name='register'),
    path('login/',auth_views.LoginView.as_view(template_name='Authentication/login.html') ,name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='Authentication/logout.html'),name='logout')
]