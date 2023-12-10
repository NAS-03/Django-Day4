from django.shortcuts import render
from courses.models import Courses
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

@csrf_exempt
def CourseView(request):
    courses = Courses.objects.all()

    return render(request,'course.html',{'courses':courses})

