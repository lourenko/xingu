
from django.db import models

import uuid


## Models ----------------------------------

class Post(models.Model):
    ""
    title = models.CharField(max_length=140)
    body = models.TextField()
    descr = models.CharField(blank=True, max_length=200)
    date = models.DateTimeField()

    def __str__(self):
        return self.title

class Course(models.Model):
    ""
    name = models.CharField(max_length=128, unique=True)
    image = models.ImageField(blank=True)
    body = models.TextField(null=True)
    nick = models.CharField(max_length=7, error_messages={'unique':"That address has already been added."}, null=True,
                                blank=True, default=uuid.uuid1)

    def __str__(self):
        return self.name

class Lesson(models.Model):
    ""
    course = models.ForeignKey(Course)
    title = models.CharField(max_length=128)
    descr = models.CharField(max_length=420, null=True)
    body = models.TextField(null=True)
    views = models.IntegerField(default=0, null=True)

    def __str__(self):
        return self.title

## -----------------------------------------

from django.contrib.auth.models import User

## User models -----------------------------

class Student(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)

    # The additional attributes we wish to include.

    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.firstname

# from django.contrib.contenttypes.models import ContentType
# from api.models import Project

# maqflux,  created = Group.objects.get_or_create(name='Máquinas de Fluxo')
# sistemas, created = Group.objects.get_or_create(name='Sistemas Térmicos 3')
# mecflu2,  created = Group.objects.get_or_create(name='Mecânica dos Fluidos 2')

# proj_add_perm = Permission.objects.get(name='Can add project')
# group.permissions.add(proj_add_perm)

# Code to add permission to group ???
# ct = ContentType.objects.get_for_model(Project)
# 
# # Now what - Say I want to add 'Can add project' permission to new_group?
# permission = Permission.objects.create(codename='can_add_project',
#                                            name='Can add project',
#                                        content_type=ct)
# new_group.permissions.add(permission)

## -----------------------------------------

## Meta classes ----------------------------
from django.contrib.auth.models import Group, Permission

class MyModel(models.Model):
    class Meta:
        permissions = (
            ('can_access_maqflux', 'Máquinas de fluxo permission description'),
            ('can_access_mecflu2', 'Mec. dos Fluidos2 permission description'),
            ('can_access_sistem3', 'Sistemas Térmicos permission description'),
        )
## -----------------------------------------


