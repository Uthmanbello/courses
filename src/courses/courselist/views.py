from django.shortcuts import render, redirect
from .models import Courselist
from .forms import CourseForm

# Create your views here.
def landing_page(request):
    return render(request, 'landing_page.html')

def course_list(request):
    courses = Courselist.objects.all()
    return render(request, 'course_list.html', {'courses': courses})

def add_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('course_list')
    else:
        form = CourseForm()

    return render(request, 'add_course.html', {'form': form})