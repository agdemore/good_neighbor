from django.contrib import admin
from models import Tag, Task, Category, Place

# Register your models here.

admin.site.register(Task)
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Place)