from multiprocessing import context
from django.shortcuts import render
import os, sys, time

from django.http import HttpResponse

def index(request):
    context = {
        'Judul' : 'Biodata',
        'h1' : 'Django',
        'menu' : [['', 'Home'], ['recent', 'Recent'], ['', 'Post']]
    }
    return render(request, 'blog/index.html', context)

def recent(request):
    return HttpResponse("RECENT BLOG")
    #context = {
    #    'Judul' : 'blog2',
    #    'h1' : 'Python'
    #}
    #return render(request, 'blog/index.html', context)
# Create your views here


    
