from django.contrib import admin

from .models import Student, SubGroup, SuperGroup


class StudentInlineGroup(admin.TabularInline):
    model = Student
    list_display = ('first_name', 'last_name', 'email')
    search_fields = ('first_name', 'last_name', 'email')
    fields = ('first_name', 'last_name', 'email')


class SubGroupInlineAdmin(admin.TabularInline):
    model = SubGroup
    list_display = ('name',)


class GroupAdmin(admin.ModelAdmin):
    inlines = (StudentInlineGroup,)


class SuperGroupAdmin(admin.ModelAdmin):
    fields = ('name',)
    inlines = (SubGroupInlineAdmin,)


admin.site.register(SuperGroup, SuperGroupAdmin)
admin.site.register(Student)
admin.site.register(SubGroup, GroupAdmin)