from django.shortcuts import render, redirect
from . models import Blog, Comment
# Create your views here.
def index(requst):
    blog= Blog.objects.all()
    context = {
    "blogs" : Blog.objects.all()
    # select * from blog
    }
    return render(requst, "test_app/index.html", context)

def blogs(request):
    # using ORM
    Blog.objects.create(title=request.POST['title'], blog=request.POST['blog'])
    # insert into blog (title, blog, created_at, updated_at) values (title, blog, now(), now())
    return redirect('/')

def comments(request, id):
    blog = Blog.objects.get(id=id)
    Comment.objects.create(comment=request.POST['comment'], blog=blog)
    return redirect('/')
