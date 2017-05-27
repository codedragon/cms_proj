import datetime
from django.contrib import admin
from django.core.urlresolvers import reverse  # Added for reverse error
from cmsblog.models import *
import logging


# create logger with module name
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
# create file handler which logs even debug messages
log_file_name = __name__ + '.log'
fh = logging.FileHandler(log_file_name)
fh.setLevel(logging.DEBUG)
# create formatter and add it to the handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
# add the handlers to the logger
logger.addHandler(fh)


class CategorizationInline(admin.TabularInline):
    """The admin interface has the ability to edit models on the same page as
    a parent model. These are called inlines.
    """
    logger.info('CategorizationInline')
    model = Category.posts.through
    # <class 'django.db.models.base.ModelBase'>
    # <class 'cmsblog.models.Category_posts'>
    # Includes:
    logger.info('type model: %s', type(model))
    logger.info('model: %s', model)
    logger.info('dir model: %s', dir(model))
    logger.info('model.category: %s', print(model.category))


def make_published(modeladmin, request, queryset):
    """Set publication date for selected posts.
    Used by: PostAdmin()
    """
    now = datetime.datetime.now()
    queryset.update(published_date=now)
    make_published.short_description = "Set publication date for selected posts"


class PostAdmin(admin.ModelAdmin):
    inlines = [
        CategorizationInline,
    ]
    list_display = (
        '__unicode__', 'author_for_admin', 'created_date', 'modified_date', 'published_date'
    )
    readonly_fields = (
        'created_date', 'modified_date',
    )
    actions = [make_published, ]

    def author_for_admin(self, obj):
        author = obj.author
        url = reverse('admin:auth_user_change', args=(author.pk,))
        name = author.get_full_name() or author.username
        link = '<a href="{}">{}</a>'.format(url, name)
        return link
    author_for_admin.short_description = 'Author'
    author_for_admin.allow_tags = True


class CategoryAdmin(admin.ModelAdmin):
    fields = ('name', 'description')
    exclude = ('posts', )


class EventAdmin(admin.ModelAdmin):
    fields = ('title', 'event_start', 'event_end')


admin.site.register(Event, EventAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)