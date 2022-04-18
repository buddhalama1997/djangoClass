from django.shortcuts import render

# Create your views here.
def djangoPage(request):
    return render(request,'course/djangoCourse.html')