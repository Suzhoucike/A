from django.contrib import admin

# Register your models here.
# admin.py
from django.contrib import admin
from alpha.models import Course
from alpha.models import CourseCategory


admin.site.register(Course)
admin.site.register(CourseCategory)

