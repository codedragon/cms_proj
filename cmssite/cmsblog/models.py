from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=128)
    text = models.TextField(blank=True)
    author = models.ForeignKey(User)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField(blank=True, null=True)

    def __unicode__(self):
        """Returns a nice, human-readable representation of the model from the
        __unicode__() method.
        """
        return self.title

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(blank=True)
    posts = models.ManyToManyField(Post, blank=True,
                                   related_name='categories')

    class Meta:
        """Model metadata is 'anything that’s not a field', such as ordering
        options (ordering), database table name (db_table), or human-readable
        singular and plural names (verbose_name and verbose_name_plural).
        None are required, and adding class Meta to a model is completely
        optional.
        """
        verbose_name_plural = 'Categories'

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name