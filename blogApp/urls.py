from django.urls import path

from .views import *

app_name = "blog"

urlpatterns = [
    path("", blog_home_view, name="blog-home"),
    path("category/<str:cat_name>/", blog_home_view, name="blog-category"),
    path("tags/<str:tag_name>/", blog_home_view, name="blog-tags"),
    path("author/<str:author_username>/", blog_home_view, name="blog-author"),
    path("search/", blog_search_view, name="blog-search"),
    path("blog-single/<int:pid>/", blog_single_view, name="blog-single"),
]
