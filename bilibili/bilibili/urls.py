"""bilibili URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from alpha import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/', views.base),
    path('base/datamanage/',views.datamanage),
    path('base/classes/', views.classes),
    path('base/map/', views.map),
    path('base/register/', views.register),
    path('base/home/',views.home),
    path('base/datamanage/coursecategory/', views.coursecategoty),
    path('base/datamanage/course/', views.course),
    path('base/datamanage/course/add/', views.addcourse),
    path('base/datamanage/course/delete/', views.deletecourse),
    path('base/datamanage/coursecategory/add/', views.addcoursecategory),
    path('base/datamanage/coursecategory/delete/', views.deletecoursecategoty),
    path('tree/', views.tree),
    path('logout/',views.logout),

    path('training-plan/', views.training_plan),
    path('test1/', views.get_courses_by_category, name='get-courses-by-category'),  # 重要
    path('get/', views.get),
    path('add_selected_courses/', views.add_selected_courses),
    path('add_elective_courses/', views.add_elective_courses),
    path('training_plan_display1/', views.training_plan_display1),
    path('training_plan_display/', views.training_plan_display),
    path('training_plan_generate/', views.Trainingplan_generate),

    path('stopmakingtrainingplan/',views.stopmakingtrainingplan),

    path('base/searchcourse/', views.searchcourse),
    path('base/searchcoursecategory/', views.searchcoursecategory),
    path('base/course/<int:nid>/edit/', views.course_edit),
    path('base/coursecategory/<int:pid>/edit/', views.coursecategory_edit),
    path('base/datamanage/course/', views.course, name='course_list'),
    path('base/datamanage/coursetegory/', views.coursecategoty, name='coursecategory_list'),

]
