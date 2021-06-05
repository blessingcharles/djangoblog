from django.urls import path
from . import views

app_name='blog'
urlpatterns = [
    path('',views.home,name='home'),
    path('aboutus/',views.about,name='about'),
    path('post/new/',views.PostCreateView.as_view(),name='postcreate'),
    path('post/<int:pk>/',views.PostDetailView.as_view(),name='postdetail'),
    path('post/<int:pk>/update',views.PostUpdateView.as_view(),name='postupdate'),
    path('post/<int:pk>/delete',views.PostDeleteView.as_view(),name='postdelete'),

]

