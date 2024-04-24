from django import template
from django_app import models

register = template.Library()


@register.filter(name="short")
def short(text):
    if len(text) > 10:
        return text[:10] + "..."
    else:
        return text


@register.simple_tag
def get_comments(post_id):
    post = models.Post.objects.get(pk=post_id)
    comments = models.Comment.objects.filter(post=post)
    return comments
