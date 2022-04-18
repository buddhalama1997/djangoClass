from django.shortcuts import render

# Create your views here.
def djangoCourse(request):
    return render(request,'course/djangoCourse.html')

def pythonCourse(request):
    return render(request,'course/pythonCourse.html')

