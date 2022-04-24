from django.shortcuts import render

from student.models import StudentDetails

# Create your views here.
def studentInfo(request):
    stu = StudentDetails.objects.all()
    return render(request,'student/studentInfo.html',{'stu':stu})