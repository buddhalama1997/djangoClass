from django.shortcuts import render

# Create your views here.

# View function for django course page
def djangoCourse(request):
    return render(request,'course/djangoCourse.html')

# View function for python course page
def pythonCourse(request):
    return render(request,'course/pythonCourse.html')