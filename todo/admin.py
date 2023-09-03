from django.contrib import admin
from .models import todoModel, todoComment

# Register your models here.
admin.site.register(todoModel)
admin.site.register(todoComment)
