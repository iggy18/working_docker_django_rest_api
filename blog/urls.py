from django.urls import path
from .views import HomePageView, DetailView, CreateBlogView, BlogUpdateView, DeleteBlogView

urlpatterns = [
    path('home/', HomePageView.as_view(), name='home'),
    path('detail/<int:pk>/', DetailView.as_view(), name='post_detail'),
    path('new/', CreateBlogView.as_view(), name='new_post'), 
    path('<int:pk>/edit/', BlogUpdateView.as_view(), name='edit_post'), 
    path('<int:pk>/delete/', DeleteBlogView.as_view(), name='delete_post')
]