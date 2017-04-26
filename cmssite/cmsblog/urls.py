from django.conf.urls import url
# from cmsblog.views import stub_view
from cmsblog.views import list_view
from cmsblog.views import detail_view


urlpatterns = [
    url(r'^$',
        list_view,# defined in views.py
        name="blog_index"),#    why is URL namespace needed here?
    url(r'^posts/(?P<post_id>\d+)/$',
        detail_view,
        name="blog_detail"),
]
