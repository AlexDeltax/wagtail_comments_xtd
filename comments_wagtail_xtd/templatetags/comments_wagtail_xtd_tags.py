from django import template


register = template.Library()


@register.inclusion_tag('comments_wagtail_xtd/partials/comments_breadcrumb.html', takes_context=True)
def comments_breadcrumb(context):
    return context
