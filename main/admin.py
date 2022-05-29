from django.contrib import admin
from main.models import Intro, Category, Project, Contact

# Register your models here.
class IntroAdmin(admin.ModelAdmin):
    pass

class CategoryAdmin(admin.ModelAdmin):
    pass

class ProjectAdmin(admin.ModelAdmin):
    pass

class ContactAdmin(admin.ModelAdmin):
    pass

admin.site.register(Intro, IntroAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Contact, ContactAdmin)