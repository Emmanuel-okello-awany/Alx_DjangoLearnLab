from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.PostListView.as_view(), name='home'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('post/new/', views.PostCreateView.as_view(), name='create_post'),  # New post creation
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='edit_post'),  # Post update
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='delete_post'),
    path('profile/', views.profile, name='profile'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('search/', views.search_posts, name='search_posts'),
    path('tag/<slug:tag_slug>/', views.posts_by_tag, name='posts_by_tag'),

        # Comment CRUD URLs
    path('post/<int:post_id>/comments/new/', views.CommentCreateView.as_view(), name='create_comment'),
    path('comment/<int:pk>/edit/', views.CommentUpdateView.as_view(), name='edit_comment'),
    path('comment/<int:pk>/delete/', views.CommentDeleteView.as_view(), name='delete_comment')
]
