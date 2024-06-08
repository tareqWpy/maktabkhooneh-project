from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.utils import timezone

from blogApp.models import Post


def blog_home_view(request, cat_name=None, author_username=None):
    posts = Post.objects.filter(published_date__lte=timezone.now(), status=1)
    if cat_name is not None:
        posts = posts.filter(category__category_name=cat_name)
    if author_username is not None:
        posts = posts.filter(author__username=author_username)

    posts = Paginator(posts, 4)
    try:
        page_number = request.GET.get("page")
        posts = posts.get_page(page_number)
    except PageNotAnInteger:
        posts = posts.get_page(1)
    except EmptyPage:
        posts = posts.get_page(1)
    context = {"posts": posts}
    return render(request, "blog/blog-home.html", context)


def blog_search_view(request):
    posts = Post.objects.filter(published_date__lte=timezone.now(), status=1)
    if request.method == "GET":
        search = request.GET.get("s")
        if search:
            search = search.lower()
            posts = posts.filter(
                Q(content__contains=search)
                | Q(author__username__contains=search)
                | Q(title__contains=search)
                | Q(category__category_name__contains=search)
            ).distinct()
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
        "author": post.author,
        "current_post": post,
        "prev_post": prev_post,
        "next_post": next_post,
    }

    counted_view(request, post)
    return render(request, "blog/blog-single.html", context)
