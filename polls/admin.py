from django.contrib import admin

from polls.models import TbSubject, TbTeacher
# Register your models here.


class TbSubjectModelAdmin(admin.ModelAdmin):
    list_display = ('no', 'name', 'intro', 'is_hot')
    search_fields = ('name',)
    ordering = ('no', )


class TeacherModelAdmin(admin.ModelAdmin):
    list_display = ('no', 'name', 'sex', 'birth', 'gcount', 'bcount', 'sno')
    search_fields = ('name', )
    ordering = ('no', )


admin.site.register(TbSubject, TbSubjectModelAdmin)
admin.site.register(TbTeacher, TeacherModelAdmin)
