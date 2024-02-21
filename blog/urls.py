from django.urls import path
from . import views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView, LastPostListView


urlpatterns = [
    path('', PostListView.as_view() , name="blog-home"),
    path("post/<int:pk>/", PostDetailView.as_view() , name="post-detail"),
    path("post/new/", PostCreateView.as_view() , name="post-create"),
    path("post/<int:pk>/update/", PostUpdateView.as_view() , name="post-update"),
    path("post/<int:pk>/delete/", PostDeleteView.as_view() , name="post-delete"),
    path("user/<str:username>/", UserPostListView.as_view(), name="user-post"),
    path("post/ultimi/", LastPostListView.as_view(), name="last-post"),
    path("bloggers/", views.bloggers, name="users-list"),
    path("about/", views.about, name="blog-about")
]