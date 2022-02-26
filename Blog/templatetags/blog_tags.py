from django import template
from Blog.models import Post
from django.db.models import Count
from django.utils.safestring import mark_safe
import markdown


register = template.Library()

@register.simple_tag #return string
def total_posts():
    return Post.published.count()

@register.inclusion_tag('blog\post\latest_post.html')
def show_latest_posts(count=5):
    latest_posts = Post.published.order_by('-publish')[:count]
    return {'latest_posts': latest_posts}

@register.simple_tag
def get_most_commented_posts(count=5):
    qs = Post.published.annotate(total_comments=Count('comments'))\
        .order_by('-total_comments')[:count]
    return qs

@register.filter(name='markdown')
def markdown_format(text):
    return mark_safe(markdown.markdown(text))
