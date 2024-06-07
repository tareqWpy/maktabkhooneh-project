from django.urls import path

from .views import *

app_name = "blog"

urlpatterns = [
    path("", blog_home_view, name="blog-home"),
    path("blog-single/<int:pid>/", blog_single_view, name="blog-single"),
    path("category/<str:cat_name>/", blog_category_view, name="blog-category"),
]
