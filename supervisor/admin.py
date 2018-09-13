from django.contrib import admin

# Register your models here.
from .models import Department, Project, Stage, Phase, Task, Issue

admin.site.register(Department)
admin.site.register(Project)
admin.site.register(Stage)
admin.site.register(Phase)
admin.site.register(Task)
admin.site.register(Issue)