from django.contrib import admin

# Register your models here.
from .models import Student, User,CourseALlocation,Lecturer






admin.site.register(User)
admin.site.register(Student)
admin.site.register(Lecturer)

class AllocattionAdmin(admin.ModelAdmin):
    list = ['lecturer']
admin.site.register(CourseALlocation,AllocattionAdmin)
