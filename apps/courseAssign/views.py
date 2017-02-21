from django.shortcuts import render, redirect
from .models import Course
# Create your views here.
def index(request):
    context = {
    "courses" : Course.objects.all()
    }
    return render(request,"courseAssign/index.html", context)

def process(request):
    if request.method == "POST":
        if request.POST['submit']== 'Add':
            Course.objects.create(course_name=request.POST['name'],description=request.POST['description'])
        return redirect('/')

def remove(request,id):
    if request.method == "POST":
        if request.POST['submit'] == "YES":
            Course.objects.filter(id=id).delete()
            return redirect('/')
        elif request.POST['submit'] =="NO":
            return redirect('/')
    else:
        course = Course.objects.get(id=id)
        context = {'course': course}
        return render(request, 'courseAssign/delete.html', context)
