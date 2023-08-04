from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Count, Sum
from .models import Courselist, Topic
from .forms import CourseForm, TopicForm

# Create your views here.
def landing_page(request):
    return render(request, 'landing_page.html')

def about(request):
    return render(request, 'about.html')

def course_list(request):
    courses = Courselist.objects.annotate(topics_count=Count('topics')).order_by('name')
    courses_count = courses.count()
    total_topics_count = Courselist.objects.aggregate(total=Count('topics'))['total']
    return render(request, 'course_list.html', {'courses': courses, 'total_topics_count': total_topics_count, 'courses_count': courses_count})

def add_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('course_list')
    else:
        form = CourseForm()

    return render(request, 'add_course.html', {'form': form})

def delete_course(request, courselist_id):
    course = get_object_or_404(Courselist, id=courselist_id)
    if request.method == 'POST':
        course.delete()
        return redirect('course_list')
    return render(request, 'delete_course.html', {'course': course})

def course_detail(request, courselist_id):
    course = get_object_or_404(Courselist.objects.prefetch_related('topics'), id=courselist_id)
    topics = course.topics.order_by('id')
    topics_count = course.topics.count()
    return render(request, 'course_detail.html', {'course': course, 'topics': topics, 'topics_count': topics_count})

def topic_detail(request, courselist_id, topic_id):
    course = get_object_or_404(Courselist.objects.prefetch_related('topics'), id=courselist_id)
    topic = get_object_or_404(Topic, id=topic_id)
    return render(request, 'topic_detail.html', {'course': course, 'topic': topic})

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

def delete_topic(request, courselist_id, topic_id):
    course = get_object_or_404(Courselist, id=courselist_id)
    topic = get_object_or_404(Topic, id=topic_id)
    if request.method == 'POST':
        topic.delete()
        return redirect('course_detail', courselist_id=course.id)
    return render(request, 'delete_topic.html', {'course': course, 'topic': topic})

def edit_topic(request, courselist_id, topic_id):
    course = get_object_or_404(Courselist, id=courselist_id)
    topic = get_object_or_404(Topic, id=topic_id)

    if request.method == 'POST':
        form = TopicForm(request.POST, instance=topic)
        if form.is_valid():
            form.save()
            return redirect('course_detail', courselist_id=course.id)
    else:
        form = TopicForm(instance=topic)

    return render(request, 'edit_topic.html', {'form': form})
