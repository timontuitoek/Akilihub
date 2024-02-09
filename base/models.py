import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True, null=True)
    name = models.CharField(max_length=100, null=True)
    bio = models.TextField(null=True)
    # avatar
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    

class Field(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    desctiption = models.TextField()
    
    def __str__(self):
        return self.name
    

class Resource(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    link = models.TextField(null=True)
    related_field = models.ForeignKey(Field, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name


class AkiliRoom(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    field = models.ForeignKey(Field, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    members = models.ManyToManyField(User, related_name='members', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name