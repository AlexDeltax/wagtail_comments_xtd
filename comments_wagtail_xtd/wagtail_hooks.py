from django.urls import reverse
from wagtail.admin.menu import MenuItem
from wagtail.core import hooks
from . import urls
from django.urls import re_path
from django.conf.urls import include
from django.utils.translation import gettext_lazy as _


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
