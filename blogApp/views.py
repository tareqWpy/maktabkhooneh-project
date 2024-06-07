from datetime import datetime

from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.utils import timezone

from blogApp.models import Post


def blog_home_view(request):
    posts = Post.objects.filter(published_date__lte=timezone.now(), status=1)
    context = {"posts": posts}
    return render(request, "blog/blog-home.html", context)


def counted_view(request, post):
    post.counted_views += 1
    post.save()
    context = {"post": post}
    return render(request, "blog/blog-single.html", context)


def blog_single_view(request, pid):
    post = get_object_or_404(Post, pk=pid, published_date__lte=timezone.now(), status=1)

    # Query for the next post
    next_post = (
        Post.objects.filter(
            published_date__gt=post.published_date,
            status=1,
            published_date__lte=timezone.now(),
        )
        .order_by("published_date")
        .first()
    )

    # Query for the previous post
    prev_post = (
        Post.objects.filter(
            published_date__lt=post.published_date,
            status=1,
            published_date__lte=timezone.now(),
        )
        .order_by("-published_date")
        .first()
    )

    context = {
        "current_post": post,
        "prev_post": prev_post,
        "next_post": next_post,
    }

    counted_view(request, post)
    return render(request, "blog/blog-single.html", context)
