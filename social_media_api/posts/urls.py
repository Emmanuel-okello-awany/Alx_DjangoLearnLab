from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet, user_feed, LikePostView, UnlikePostView

router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path("feed/", user_feed, name="user_feed"),
    path('posts<int:pk>/like/', LikePostView.as_view(), name='like-post'),
    path('posts<int:pk>/unlike/', UnlikePostView.as_view(), name='unlike-post'),
]
