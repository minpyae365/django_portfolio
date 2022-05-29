from django.contrib import admin
from exercises.models import  Category, Project

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    pass

class ProjectAdmin(admin.ModelAdmin):
    pass

admin.site.register(Category, CategoryAdmin)
admin.site.register(Project, ProjectAdmin)
