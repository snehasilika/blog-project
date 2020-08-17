"""BlugProject1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from blog import views
from blog.models import Post
from django.views.generic import ListView

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('',views.post_list_view),
    path('',views.PostListView.as_view()),
    #path('detail',views.post_detail_view),
    #path('',views.ListView.as_view(queryset=Post.objects.filter(status='published'),paginate_by=1,template_name='post_list.html')),
    path('detail/<int:year>/<int:month>/<int:day>/<str:post>/',views.post_detail_view,name='post_detail'),
    path('<id>/share/',views.mail_send_view)

]
