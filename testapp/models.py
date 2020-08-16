from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    STATUS_CHOICE=(('draft','Draft'),('published','Published'))
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=256,unique_for_date='publish')
    author = models.ForeignKey(User,related_name='blog_post',on_delete=models.CASCADE)
    body=models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,choices=STATUS_CHOICE,default='draft')
    
    
    class Meta:
        ordering=('-publish',)
        def __str__(self):
            return self.title

    def get_absolute_url(self): 
            return reverse('post_detail',args=[self.publish.year,self.publish.month,self.publish.day,self.slug])

