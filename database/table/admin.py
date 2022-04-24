from django.contrib import admin
from table.models import Student
# Register your models here.

admin.site.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ( 'stuid', 'stuname','stuemail')