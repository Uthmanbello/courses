from django.shortcuts import render, redirect, get_object_or_404
from .models import Courselist
from .forms import CourseForm, TopicForm

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

def course_detail(request, courselist_id):
    # course = get_object_or_404(Courselist, id=courselist_id)
    course = get_object_or_404(Courselist.objects.prefetch_related('topics'), id=courselist_id)
    return render(request, 'course_detail.html', {'course': course})

def add_topics(request, courselist_id):
    course = get_object_or_404(Courselist, id=courselist_id)

    if request.method == 'POST':
        form = TopicForm(request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.course = course
            topic.save()
            return redirect('course_detail', courselist_id=course.id)
    else:
        form = TopicForm()

    return render(request, 'add_topics.html', {'form': form})
