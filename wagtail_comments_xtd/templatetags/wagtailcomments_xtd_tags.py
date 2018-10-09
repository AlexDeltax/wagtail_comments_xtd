from django import template


register = template.Library()


@register.inclusion_tag('wagtailcomments_xtd/partials/comments_breadcrumb.html', takes_context=True)
def comments_breadcrumb(context):
    return context
