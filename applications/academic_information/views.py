# from django.shortcuts import render

from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Student_attendance

def homepage(request):
    context = {}

    return render(request, "ais/ais.html", context)

def mark_attendance(request):
    st_id=request.POST['student_id']
    c_id=request.POST['course_id']
    date_field=request.POST['date']
    status=request.POST['status']
    st_attend=Student_attendance.objects.get(student_id=st_id)
    if(status=='present'):
        st_attend.current_attend=st_attend.current_attend+1
    st_attend.total_attend=st_attend.total_attend+1
    return HttpResponseRedirect('')


def add_attendance(request):
    st_id = request.POST['student_id']
    c_id = request.POST['course_id']
    st_attend=Student_attendance()
    st_attend.student_id=st_id
    st_attend.course_id=c_id
    st_attend.save()
    return HttpResponseRedirect('')



