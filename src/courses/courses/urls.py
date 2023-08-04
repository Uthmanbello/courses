"""
URL configuration for courses project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from courselist.views import landing_page, about, course_list, add_course, course_detail, topic_detail, add_topics, delete_course, delete_topic, edit_topic

urlpatterns = [
    path('', landing_page, name='landing_page'),
    path('about/', about, name='about'),
    path('admin/', admin.site.urls),
    path('courses/', course_list, name='course_list'),
    path('add_course/', add_course, name='add_course'),
    path('courses/<int:courselist_id>/', course_detail, name='course_detail'),
    path('courses/<int:courselist_id>/<int:topic_id>', topic_detail, name='topic_detail'),
    path('courses/<int:courselist_id>/add_topic/', add_topics, name='add_topics'),
    path('courses/<int:courselist_id>/delete/', delete_course, name='delete_course'),
    path('courses/<int:courselist_id>/<int:topic_id>/delete_topic/', delete_topic, name='delete_topic'),
    path('courses/<int:courselist_id>/<int:topic_id>/edit_topic/', edit_topic, name='edit_topic'),
]

