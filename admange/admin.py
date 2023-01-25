from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import StudentList, SubjectList, Fraction

# Register your models here.


class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'sex',
                    'created_time', 'update_time')

    '''filter options'''
    list_filter = ('id', )

    '''10 items per page'''
    list_per_page = 10


class SubjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_time', 'update_time')


class FractionAdmin(admin.ModelAdmin):
    list_display = ('id', 'student', 'subject', 'fraction')


admin.site.register(StudentList, StudentAdmin)
admin.site.register(SubjectList, SubjectAdmin)
admin.site.register(Fraction, FractionAdmin)
