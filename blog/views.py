from multiprocessing import context
from django.shortcuts import render

from django.http import HttpResponse
from .models import Post

def index(request):
    db = Post.objects.all()
    context = {
        'Judul' : 'Blog Saya',
        'h1' : 'Tentang Saya',
        'Nama' : 'Rakasona',
        'NPM' : '1204056',
        'Asal' : 'Kuningan, Jawa Barat',
        'Email' : 'rakasona472@gmail.com',
        'HP' : '085171547599',
        'Umur' : '20',
        'Desc' : 'Mahasiswa, keren adalah passion',
        'title':'Blog',
        'heading':'Blog',
        'subheading':'postingan',
        'post': db,
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