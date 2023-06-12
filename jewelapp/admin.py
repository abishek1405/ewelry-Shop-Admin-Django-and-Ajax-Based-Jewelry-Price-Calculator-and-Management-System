from django.contrib import admin

# Register your models here.
from .models import Student, User,CourseALlocation,Lecturer,Dealer,Seldealer





admin.site.register(Seldealer)
admin.site.register(User)
admin.site.register(Student)
admin.site.register(Lecturer)
admin.site.register(Dealer)

class AllocattionAdmin(admin.ModelAdmin):
    list = ['lecturer']
admin.site.register(CourseALlocation,AllocattionAdmin)
