from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import *


# Create your views here.


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def post_list(request):
    posts = Post.objects.filter(tag='self')
    return HttpResponse(posts)
def post_detail(request,id):
    try:
        posts = Post.objects.get(id=id)
        return HttpResponse(posts)
    except:
        raise Http404("not found")