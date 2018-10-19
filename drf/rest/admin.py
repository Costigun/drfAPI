from django.contrib import admin
from .models import *
admin.site.register(Branches)
admin.site.register(Contacts)

class EzoneInline(admin.StackedInline):
    model = Contacts
    extra = 0
    print(123)
class BranchesInline(admin.StackedInline):
    model = Branches
    extra = 0

class EzoneAdmin(admin.ModelAdmin):
    save_on_top = True
    inlines = [
        EzoneInline,BranchesInline
    ]
admin.site.register(Ezone,EzoneAdmin)


