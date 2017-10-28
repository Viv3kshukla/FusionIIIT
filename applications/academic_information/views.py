# from django.shortcuts import render
from django.shortcuts import render
from .models import Student_attendance,Course,Student
from django.http import HttpResponseRedirect

def homepage(request):
    context = {}

    return render(request, "ais/ais.html", context)

def add_attendance(request):
    student_attend=Student_attendance()
    student_attend.student_id=request.POST.get('student_id')
    print('student_id ',student_attend.student_id)
    student_attend.course_id=request.POST.get('course_id')
    student_attend.present_attend=request.POST.get('present_attend')
    student_attend.total_attend=request.POST.get('total_attend')
    student_attend.save()
    return HttpResponseRedirect('')


