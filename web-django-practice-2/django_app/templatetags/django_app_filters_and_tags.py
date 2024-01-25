from django import template
from django_app import models

register = template.Library()


@register.filter(name="format_price")
def format_price(price):
    return f"{price:,}".replace(",", " ")


@register.filter(name="short_description")
def short_description(text):
    if len(text) > 100:
        return text[:100] + "..."
    else:
        return text


@register.simple_tag(takes_context=True)
def rating(context, id):
    product = models.Product.objects.get(id=id)
    ratings = models.Rating.objects.all().filter(product=product)
    return ratings.filter(is_like=True).count() - ratings.filter(is_like=False).count()


@register.simple_tag(takes_context=True)
def rating_count(context, user):
    return models.Rating.objects.filter(author=user, is_like=True).count()


@register.simple_tag(takes_context=True)
def views_count(context, id):
    product = models.Product.objects.get(id=id)
    return product.views_count


@register.simple_tag(takes_context=True)
def is_favorite(context, id):
    product = models.Product.objects.get(id=id)
    try:
        favorite = models.Favorite.objects.get(
            user=context["request"].user, product=product
        )
        return True
    except Exception as error:
        print(error)
        return False


@register.simple_tag(takes_context=True)
def favorite_count(context):
    return models.Favorite.objects.filter(user=context.request.user).count()
