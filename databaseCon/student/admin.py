from django.contrib import admin

from student.models import StudentDetails

# Register your models here.
admin.site.register(StudentDetails)
class StudentDetailsAdmin(admin.ModelAdmin):
    list_display = ['id', 'stuid', 'stuname','stuemail',]