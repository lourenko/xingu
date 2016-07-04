

from django.contrib import admin
from django.contrib.auth.models import User

from mysite.models import Post, Lesson, Course
from mysite.models import Student


admin.site.register(Post)
admin.site.register(Lesson)
admin.site.register(Course)

## Users profiles
admin.site.register(Student)

