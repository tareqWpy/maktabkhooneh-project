from django import template
from django.utils import timezone

from blogApp.models import Post

register = template.Library()


@register.inclusion_tag("website/home-posts.html")
def home_latest_post():
    posts = Post.objects.filter(status=1, published_date__lte=timezone.now()).order_by(
        "-published_date"
    )[:6]
    return {"posts": posts}
