from django.contrib import admin
from blog.models import Post,Comment

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ['title','slug','author','body','publish','created','updated','status']
    list_filter = ('status',)
    #search_fields = ['author__username','title']#author is user fieldnamr in Auth table 
    prepopulated_fields={'slug':('title',)}
    #raw_id_fields=('author',)
    date_hierarchy='publish'
    ordering = ['status','publish']

class CommentAdmin(admin.ModelAdmin):
    list_display=('name','email','post','body','created','updated','active')
    list_filter=('active','created','updated')
    search_fields=('name','email','body') 


admin.site.register(Post,PostAdmin)
admin.site.register(Comment,CommentAdmin) 

