from django.contrib import admin
from testapp.models import Post

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ['title','slug','author','body','publish','created','updated','status']
    list_filter = ('status',)
    search_fields = ['author__username','title']#author is user fieldnamr in Auth table 
    prepopulated_fields={'slug':('title',)}
    raw_id_fields=('author',)
    date_hierarchy='publish'
    ordering = ['status','publish']


admin.site.register(Post,PostAdmin)

