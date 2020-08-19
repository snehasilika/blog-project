from django.shortcuts import render,get_object_or_404
from blog.models import Post,Comment
from django.core.paginator import PageNotAnInteger,Paginator,EmptyPage
from django.views.generic import ListView
from django.core.mail import send_mail
from blog.forms import EmailSendForm,CommentForm
from taggit.models import Tag 
from django.db.models import Count 

# Create your views here.

def post_list_view(request,tag_slug=None):
        post_list=Post.objects.all()
        tag=None
        if tag_slug:
           tag=get_object_or_404(Tag,slug=tag_slug)
           post_list=post_list.filter(tags__in=[tag]) 
        paginator=Paginator(post_list,2)
        page_number=request.GET.get('page')
        try:
            post_list=paginator.page(page_number) 
        except PageNotAnInteger: 
            post_list=paginator.page(1) 
        except EmptyPage:
            post_list=paginator.page(paginator.num_pages)
        return render(request,'post_list.html',{'post_list':post_list,'tag':tag})
class PostListView(ListView):
    model=Post
    paginate_by=1
    template_name='post_list.html'

def post_detail_view(request,year,month,day,post):
#def post_detail_view(request):
    #post_detail=Post.objects.all()
    post_detail=get_object_or_404(Post,slug=post,status='published',publish__year=year,publish__month=month,publish__day=day) 
    post_tags_ids=post_detail.tags.only('slug')
    similar_posts=Post.objects.filter(tags__in=post_tags_ids).exclude(id=post_detail.id)
    similar_posts=similar_posts.annotate(same_tags=Count('tags')).order_by('-same_tags','publish')[:4] 
    comments=post_detail.comments.filter(active=True) 
    csubmit=False
    if request.method=='POST': 
        form=CommentForm(data=request.POST) 
        if form.is_valid(): 

            new_comment=form.save(commit=False)
            new_comment.post=post_detail
            new_comment.save()
            csubmit=True
    else:
        form=CommentForm()
    return render (request,'post_detail.html',{'post_detail':post_detail,'form':form,'comments':comments,'csubmit':csubmit,'similar_posts':similar_posts})

#SEND MAIL FUNCTION
def mail_send_view(request,id):
    post=get_object_or_404(Post,id=id,status='published') 
    sent = False
    if request.method=='POST':
      form = EmailSendForm(request.POST)
      if form.is_valid():
            cd = form.cleaned_data
            post_url=request.build_absolute_uri(post.get_absolute_url()) 
            subject='{}({}) recommends you to read "{}"'.format(cd['name'],cd['email'],post.title)
            message='Read Post At: \n {}\n\n{}\' Comments:\n{}'.format(post_url,cd['name'],cd['comments']) 
            send_mail(subject,message,'sneha@blog.com',[cd['to']])
            sent=True
    else:
            form=EmailSendForm() 
    return render (request,'sharedbymail.html',{'post':post,'form':form,'sent':sent})