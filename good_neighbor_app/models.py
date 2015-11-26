from django.db import models
from django.contrib.auth.models import User

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
    category = models.ForeignKey(Category, related_name='tasks')
    tags = models.ManyToManyField(Tag, related_name='tags')
    class Meta:
        verbose_name = 'Task'
    def __unicode__(self):
        return self.title