from django.contrib import admin
from . models import Task
# Register your models here.
class TaskModel(admin.ModelAdmin):
    list_display=['title']

admin.site.register(Task,TaskModel)
