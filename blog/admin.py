from django.contrib import admin
from blog.models import Post
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ['title','slug','body','author','publish','created','updated','status']
    list_filter = ('status','created','publish','author')
    prepopulated_fields = {'slug':('title','status','author')}#datetime field is not taking(publish) and giving error for created(system taken)
    search_fields = ('title','body','author__username')# __primary key of auth_user table
    raw_id_fields = ('author',) #must be a foreign key or a many-to-many field
    date_hierarchy ='publish'
    ordering = ['status','publish']

admin.site.register(Post,PostAdmin)
     