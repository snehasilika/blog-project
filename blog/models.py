from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from taggit.managers import TaggableManager 
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
    tags=TaggableManager()

    
    
    class Meta:
        ordering=('-publish',)
        def __str__(self):
            return self.title

    def get_absolute_url(self): 
            return reverse('post_detail',args=[self.publish.year,self.publish.month,self.publish.day,self.slug])

class Comment(models.Model):
     post=models.ForeignKey(Post,related_name='comments',on_delete=models.CASCADE) 
     name=models.CharField(max_length=32)
     email=models.EmailField()
     body=models.TextField()
     created=models.DateTimeField(auto_now_add=True)
     updated=models.DateTimeField(auto_now=True)
     active=models.BooleanField(default=True)

     class Meta:
        ordering=('-created',)
        def __str__(self):
             return 'Commented By {} on {}'.format(self.name,self.post) 



    
