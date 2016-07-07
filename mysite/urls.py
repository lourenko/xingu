


from django.conf.urls import patterns, url
from mysite import views
from mysite.models import Post

urlpatterns = [
        url(r'^$', views.index, name='index'),
        #url(r'^$', views.PostListView.as_view(), name='index'),
        #url(r'^$', ListView.as_view(queryset=Post.objects.all().order_by("-date")[:12], template_name='mysite/post.html')),
        url(r'^about/$', views.about, name='about'),
        url(r'^courses/page(?P<mat>\d+)/$', views.courses, name='courses'),
        url(r'^login/$', views.user_login, name='login'),
        url(r'^blog/(?P<pk>\d+)$', views.PostDetailView.as_view()),
        url(r'^logout/$', views.user_logout, name='logout'),
        ]

