# blog/urls.py
from django.urls import path
from . import views

app_name = 'blog'  # Ensure the namespace is set

urlpatterns = [
    path('', views.home, name='home'), 
    path('posts/', views.post_list, name='post_list'), 
    path('register/', views.register, name='register'), 
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
    path('comment/edit/<int:comment_id>/', views.edit_comment, name='edit_comment'),
    path('comment/delete/<int:comment_id>/', views.delete_comment, name='delete_comment'),
]
