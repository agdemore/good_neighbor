from django.contrib import admin
from models import Tag, Task, Category

# Register your models here.

admin.site.register(Task)
admin.site.register(Tag)
admin.site.register(Category)