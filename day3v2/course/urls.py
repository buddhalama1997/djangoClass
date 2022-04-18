from django.urls import path
from . import views
urlpatterns  =[
    path('django/',views.djangoCourse),
    path('python/',views.pythonCourse),
]