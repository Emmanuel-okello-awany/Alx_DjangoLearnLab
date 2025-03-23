from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.PostListView.as_view(), name='home'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('post/create/', views.PostCreateView.as_view(), name='create_post'),
    path('post/<int:pk>/edit/', views.PostUpdateView.as_view(), name='edit_post'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='delete_post'),
    path('profile/', views.profile, name='profile'),
    path('search/', views.search_posts, name='search_posts'),
    path('tag/<slug:tag_slug>/', views.posts_by_tag, name='posts_by_tag'),
]
