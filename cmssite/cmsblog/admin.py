import datetime
from django.contrib import admin
from django.core.urlresolvers import reverse  # Added for reverse error
from cmsblog.models import Post
from cmsblog.models import Category


class CategorizationInline(admin.TabularInline):
    """The admin interface has the ability to edit models on the same page as
    a parent model. These are called inlines.
    """
    model = Category.posts.through


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
    exclude = ('posts', )


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)