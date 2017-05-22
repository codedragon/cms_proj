from django.conf.urls import url
# from cmsblog.views import stub_view
from cmsblog.views import *


urlpatterns = [
    url(r'^$',  #wtf? not anything and end?
        list_view,  # as index.html; we should use '
        name="blog_index"),  # why is URL namespace needed here?
    url(r'^posts/(?P<post_id>\d+)/$',  # 'posts/16/'
        detail_view,  # todo 'refactor: blog_detail'
        name="blog_detail"),
    url(r'^post/index/$',  # 'post/index/'
        post_index,
        name='post_index'),
    url(r'^post/new/$',  # 'post/new/'
        post_new,
        name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$',  #post/15/edit/
        post_edit,
        name='post_edit'),
    url(r'^event/index/$',  # 'event/index/'
        event_index,
        name='event_index'),
    url(r'^talk/index/$',  # 'talk/index/'
        talk_index,
        name='talk_index'),
    url(r'^speaker/index/$',  # 'speaker/index/'
        speaker_index,
        name='speaker_index'),
    url(r'^venue/index/$',  # 'venue/index/'
        venue_index,
        name='venue_index'),
]
