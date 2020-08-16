from django.shortcuts import render,get_object_or_404
from testapp.models import Post
from django.core.paginator import PageNotAnInteger,Paginator,EmptyPage
from django.views.generic import ListView

# Create your views here.

def post_list_view(request):
        post_list=Post.objects.all()
        paginator=Paginator(post_list,2)
        page_number=request.GET.get('page')
        try:
            post_list=paginator.page(page_number) 
        except PageNotAnInteger: 
            post_list=paginator.page(1) 
        except EmptyPage:
            post_list=paginator.page(paginator.num_pages)
        return render(request,'post_list.html',{'post_list':post_list})
class PostListView(ListView):
    model=Post
    paginate_by=3
    template_name='post_list.html'

def post_detail_view(request,year,month,day,post):
#def post_detail_view(request):
    #post_detail=Post.objects.all()
    post_detail=get_object_or_404(Post,slug=post,publish__year=year,publish__month=month,publish__day=day) 
    return render (request,'post_detail.html',{'post_detail':post_detail})

