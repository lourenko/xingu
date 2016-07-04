


from django.conf.urls import patterns, url
from mysite import views
from django.views.generic import ListView, DetailView
from mysite.models import Post

urlpatterns = [
        url(r'^$', views.index, name='index'),
        #url(r'^$', views.PostListView.as_view(), name='index'),
        #url(r'^$', ListView.as_view(queryset=Post.objects.all().order_by("-date")[:12], template_name='mysite/post.html')),
        url(r'^post/$', views.post, name='post'),
        url(r'^about/$', views.about, name='about'),
        url(r'^courses/page(?P<num>\d+)/$', views.courses, name='courses'),
        url(r'^login/$', views.user_login, name='login'),
        #url(r'^(?P<pk>\d+)$', views.courses, name='courses'),
        url(r'^logout/$', views.user_logout, name='logout'),
        ]

