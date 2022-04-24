from django.shortcuts import render
from table.models import Student
# Create your views here.
def studentInfo(request):
    stud = Student.objects.all()
    return render(request,'table/studentDetails.html',{'stud':stud})