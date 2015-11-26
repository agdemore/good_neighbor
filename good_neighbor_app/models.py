from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='Name of category')
    title = models.CharField(max_length=50, verbose_name='Title of category')
    class Meta:
        verbose_name = 'Category'
    def __unicode__(self):
        return self.title


class Tag(models.Model):
    name = models.CharField(max_length=50, verbose_name='Name of tag')
    title = models.CharField(max_length=50, verbose_name='Title of tag')
    class Meta:
        verbose_name = 'Tag'
    def __unicode__(self):
        return self.title


class Task(models.Model):
    user = models.ForeignKey(User, related_name='tasks')
    title = models.CharField(max_length=50, verbose_name='Title of task')
    description = models.TextField()
    create_date = models.DateTimeField(verbose_name='date of creation')
    # end_date = models.DateTimeField(blank=True, verbose_name='date of complete')
    category = models.ForeignKey(Category, related_name='tasks')
    tags = models.ManyToManyField(Tag, related_name='tags')
    rate = models.ImageField(default=0, verbose_name='rate of task')
    class Meta:
        verbose_name = 'Task'
    def __unicode__(self):
        return self.title


class Place(models.Model):
    users = models.ManyToManyField(User, related_name='users')
    address = models.CharField(max_length=150, verbose_name='Address of place')
    tasks = models.ManyToManyField(Task, related_name='tasks')
    start_live = models.DateTimeField()
    class Meta:
        verbose_name = 'Place'
    def __unicode__(self):
        return self.address