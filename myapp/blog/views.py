from django.shortcuts import render,redirect
from django.http import HttpResponse ,Http404
from django.urls import reverse
import logging
from blog.models import Post

# posts=[
#        {'id':1,'title':'Post 1','Content':'Content of post 1','text':'Sports'},
#       {'id':2,'title':'Post 2','Content':'Content of post 2','text':'Development'},
#      {'id':3,'title':'Post 3','Content':'Content of post 3','text':'Engineering'},
#     {'id':4,'title':'Post 4','Content':'Content of post 4','text':'Travel'}
#]

# Create your views here.
def index(request):
    blog_title="Latest Posts"
    posts=Post.objects.all()
    return render(request,'index.html',{'blog_title': blog_title,'posts':posts})

def detail(request,post_id):
    try:
        # post=next((item for item in posts if item['id']==int(post_id)),None)
        post= Post.objects.get(id=post_id)
        #logger=logging.getLogger("TESTING")
        #logger.debug(f'Post variable is{post}')
    except Post.DoesNotExist:
        raise Http404("Post Does not exist!!!")
    return render(request,'detail.html',{'post':post})

def profile(request,pre_id):
    return HttpResponse(f"profile page ={pre_id}")

def old_url_redirect(request):
    return redirect(reverse('blog:new_page_url'))

def new_url_view(request):
    return HttpResponse("This is new url")