from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Posts,PostDetail
from django.core.paginator import Paginator
from . import forms
# Create your views here.

def post(request,num = 1):
    #obj =Posts.objects.all()[:5]
    limit = 2
    posts = Posts.objects.filter(is_publish=1).order_by('publish_date')
    paginator = Paginator(posts, limit)

    if 'page' in request.GET:
        page = request.GET.get('page')
    else :
         page = num
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)
    subcsribe = forms.Subscribe()
    
    context = {
        'posts': queryset,
        'subscribe' : subcsribe
    }
    # print("***********************")
    return render(request, 'index2.html', context)
    #return HttpResponse("<h1> khan </h1>")


def post_detail_view(request,slug):
    # b1 = Posts.objects.get(slug=slug)
    # data = b1.postdetail_set.all()
    post = Posts.objects.get(slug=slug)
    post_detail = PostDetail.objects.filter(post = post)
    context = {
        'posts': post,
        'postDetail' : post_detail
    }
    print("========================")
   
    return render(request, 'blog-post.html', context)

def about(request):
    return render(request, 'about.html', {})


def subscribe(request):
    if request.method == 'POST':
        form = forms.Subscribe(request.POST)
        email = request.POST['email']
        return redirect('post')
    else:
        return redirect('post')