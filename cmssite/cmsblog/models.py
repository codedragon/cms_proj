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
        """What will print"""
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


class Talk(models.Model):
    # Referenced by Event so must come above
    title = models.CharField(max_length=128)
    abstract = models.TextField(blank=True)
    # keywords

    def __unicode__(self):
        """Returns a nice, human-readable representation of the model from the
        __unicode__() method.
        """
        return self.title

    def __str__(self):
        return self.title


class Venue(models.Model):
    # References Event so must come after
    name = models.CharField(max_length=128)
    address = models.CharField(max_length=128)
    city = models.CharField(max_length=128)
    state = models.CharField(max_length=128)
    zip = models.CharField(max_length=128)
    contact_name = models.CharField(max_length=128, blank=True)
    contact_phone = models.CharField(max_length=128, blank=True)
    contact_email = models.CharField(max_length=128, blank=True)

    def __unicode__(self):
        """Returns a nice, human-readable representation of the model from the
        __unicode__() method.
        """
        return self.name

    def __str__(self):
        return self.name


class Event(models.Model):
    title = models.CharField(max_length=128)
    # todo start time, end time
    # event_time = models.DateTimeField(auto_now_add=False)
    event_start = models.DateTimeField(auto_now_add=False)
    event_end = models.DateTimeField(auto_now_add=False)
    # todo test end > start and end - start < 4 hours
    talks = models.ManyToManyField(Talk, blank=True)
    venue = models.ForeignKey(Venue)  # 'venue_id'

    def __unicode__(self):
        """Returns a nice, human-readable representation of the model from the
        __unicode__() method.
        """
        return self.title

    def __str__(self):
        return self.title


class Speaker(models.Model):
    name = models.CharField(max_length=128)
    phone = models.CharField(max_length=128)
    email = models.CharField(max_length=128)
    bio = models.TextField(blank=True)

    def __unicode__(self):
        """Returns a nice, human-readable representation of the model from the
        __unicode__() method.
        """
        return self.name

    def __str__(self):
        return self.name
