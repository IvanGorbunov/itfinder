from django.db import models
import uuid

from projects.choices import Vote
from users.models import User


class Tag(models.Model):
    """ Модель: Теги проектов """
    name = models.CharField(max_length=100)
    slug = models.SlugField()
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.name


class Project(models.Model):
    """ Модель: Проекты """
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    image = models.ImageField(null=True, blank=True, default="project_images/default.jpg", upload_to='project_images')
    description = models.TextField(null=True, blank=True)
    tags = models.ManyToManyField(Tag, blank=True)
    total_votes = models.IntegerField(default=0, null=True, blank=True)
    votes_ratio = models.IntegerField(default=0, null=True, blank=True)
    demo_link = models.CharField(max_length=500, null=True, blank=True)
    source_link = models.CharField(max_length=500, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    owner = models.ForeignKey(
        User, null=True, blank=True, on_delete=models.CASCADE)

    developers = models.ManyToManyField(
        User, verbose_name='Разработчики', related_name='projects', blank=True)

    def __str__(self):
        return self.title


class Review(models.Model):
    """ Модель: Просмотры """
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    review_text = models.TextField(null=True, blank=True)
    value = models.CharField(max_length=200, choices=Vote.CHOICES)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.value
