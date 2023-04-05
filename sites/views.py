from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from .models import BlogModel, BlogModel2

# Create your views here.
def helloworldfunc(request):
    return HttpResponse('hello world')

class BlogList(ListView):
    template_name = 'list.html'
    model = BlogModel

class BlogList2(ListView):
    template_name = 'list.html'
    model = BlogModel2
