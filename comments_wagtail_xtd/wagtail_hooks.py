from django.urls import reverse
from wagtail.admin.menu import MenuItem
from wagtail.core import hooks
from wagtail.admin.site_summary import SummaryItem
from . import urls
from django.urls import re_path
from django.conf.urls import include
from django.utils.translation import gettext_lazy as _
from django_comments_xtd import get_model as get_comment_model


XtdComment = get_comment_model()


@hooks.register('register_admin_urls')
def register_admin_urls():
    return [
        re_path(r'^comments/', include(urls)),
    ]


@hooks.register('register_admin_menu_item')
def register_styleguide_menu_item():
    return MenuItem(
        _('Comments'),
        reverse('comments_wagtail_xtd_pages'),
        classnames='icon icon-fa-comments-o',
        order=1000
    )


class CommentsSummaryItem(SummaryItem):
    order = 400
    template = "comments_wagtail_xtd/comments_summary.html"

    def get_context(self):
        total_comments = XtdComment.objects.all().count()
        return {
            "sum_title": _('Comments'),
            "total_comments": total_comments,
        }


@hooks.register("construct_homepage_summary_items")
def add_summary_item(request, items):
    items.append(CommentsSummaryItem(request))
