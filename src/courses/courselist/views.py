from django.shortcuts import render
from .models import Courselist

# Create your views here.
def landing_page(request):
    return render(request, 'landing_page.html')

def course_list(request):
    courses = Courselist.objects.all()
    return render(request, 'course_list.html', {'courses': courses})