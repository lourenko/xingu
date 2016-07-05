#! -.- coding:utf8 -.-


from django.views import generic
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponseRedirect, HttpResponse

from mysite.models import Post
from mysite.models import Course, Lesson


from django.views.generic import ListView, DetailView

class PostDetailView(DetailView):
    model = Post
    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context['post_name'] = self.object.title
        return context

    def get_template_names(self, **kwargs):
        name = super(PostDetailView, self).get_template_names(**kwargs)
        name = "mysite/post.html"
        return name

class CourseDetailView(DetailView):
    model = Post
    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context['post_name'] = self.object.title
        return context

    def get_template_names(self, **kwargs):
        name = super(PostDetailView, self).get_template_names(**kwargs)
        name = "mysite/post.html"
        return name

def index(request):
    "Minha página inicial"

    lista = Post.objects.all().order_by("-date")[:12]
    contexto = {'posts':lista, 'site_name':r'Sinóptico', 'block_name':r'Main', 'post_name':'Welcome'}
    return render(request, "mysite/index.html", contexto)

def about(request):
    "Sobre o site"

    next = ""
    if request.GET:
        next = request.GET['next']

    contexto = {'post_name':'About', 'next':next}

    return render(request, "mysite/about.html", contexto)

def post(request):
    "Minha página inicial"

    contexto = {'test': "Apenas um teste!", 'site_name':r'Sinóptico', 'block_name':r'Main'}
    return render(request, "mysite/post.html", contexto)

@login_required
def courses(request, num):
    "Course pages"

    Courses = Course.objects.order_by('name')
    perms = request.user.get_group_permissions()
    groups = request.user.groups.all()

    ok = False
    courses = []
    if len(groups):
        for g in groups:
            perm = g.permissions.all()[0].codename
            for c in Courses:
                if c.nick in perm:
                    courses.append(c)

        try:
            course = courses[int(num)-1]

            lessons = course.lesson_set.all()
            contexto = {'courses':courses, 'num':num, 'site_name':r'Sinóptico',
                        'current':course,  'lessons':lessons}

            return render(request, "mysite/courses.html", contexto)

        except: pass

    return redirect('/mysite')

def user_login(request):
    ""

    next = ""
    if request.GET:
        next = request.GET['next']

    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
                # We use request.POST.get('<variable>') as opposed to request.POST['<variable>'],
                # because the request.POST.get('<variable>') returns None, if the value does not exist,
                # while the request.POST['<variable>'] will raise key error exception
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
        user = authenticate(username=username, password=password)

        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        if user:
            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                login(request, user)
                if next == "":
                    return HttpResponseRedirect('/mysite')
                else:
                    request.user = user
                    return HttpResponseRedirect(next)
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Your account is disabled.")
        else:
            # Bad login details were provided. So we can't log the user in.
            print("Invalid login details: {0}, {1}".format(username, password))
            return HttpResponse("Invalid login details supplied.")

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render(request, 'mysite/login.html', {'next':next})

@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)

    # Take the user back to the homepage.
    return HttpResponseRedirect('/mysite')


