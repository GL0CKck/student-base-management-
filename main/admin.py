from django.contrib import admin
from .models import SuperGroup, Student, SubGroup


class StudentInlineGroup(admin.TabularInline):
    model = Student
    list_display = ('first_name', 'last_name', 'email')
    search_fields = ('first_name', 'last_name', 'email')
    fields = ('first_name', 'last_name', 'email')


class GroupAdmin(admin.ModelAdmin):
    inlines = (StudentInlineGroup,)


class SuperGroupAdmin(admin.ModelAdmin):
    fields = ('name',)


admin.site.register(SuperGroup, SuperGroupAdmin)
admin.site.register(Student)
admin.site.register(SubGroup, GroupAdmin)