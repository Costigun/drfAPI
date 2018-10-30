from django.contrib import admin
from .models import *


admin.site.register(Branches)
admin.site.register(Contacts)
admin.site.register(Category)

class CourseInline(admin.StackedInline):
    model = Contacts
    extra = 0
    exclude = ['Course']

class BranchesInline(admin.StackedInline):
    model = Branches
    extra = 0

class CourseAdmin(admin.ModelAdmin):
    save_on_top = True
    inlines = [
        CourseInline,BranchesInline
    ]

admin.site.register(Course,CourseAdmin)


