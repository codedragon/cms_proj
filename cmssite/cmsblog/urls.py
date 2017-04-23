from django.conf.urls import url
# from cmsblog.views import stub_view
from cmsblog.views import list_view
from cmsblog.views import detail_view


urlpatterns = [
    url(r'^$',
        list_view,
        name="blog_index"),
    url(r'^posts/(?P<post_id>\d+)/$',
        detail_view,
        name="blog_detail"),
]
