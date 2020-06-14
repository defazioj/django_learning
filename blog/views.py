from django.shortcuts import render
# from django.http import HttpResponse


posts = [
    {
        'author': 'JeffreyD',
        'title': 'Blog Post 1',
        'content': 'First Post Content',
        'date_posted': 'June 14, 2020'
    },
    {
        'author': 'JaneDoe',
        'title': 'Blog Post 2',
        'content': 'Second Post Content',
        'date_posted': 'June 15, 2020'
    },
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)
    # return HttpResponse('<h1>Blog Home</h1>')


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
