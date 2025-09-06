from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)

    class Tags(models.TextChoices):
        self = 'sl' , 'self'
        bisnust = 'bsn' , 'bsn'
        study = 'std' , 'std'


    content = models.TextField()

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    tag = models.CharField(choices=Tags.choices, max_length=20,default='self')

    slug = models.SlugField(max_length=100)

    pub_date = models.DateTimeField(default=timezone.now)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)



    class Meta:
        ordering = ['-pub_date']
        indexes = [models.Index(fields=['-pub_date'])]

    def __str__(self):
        return self.title
