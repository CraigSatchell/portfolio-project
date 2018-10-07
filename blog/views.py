from django.shortcuts import render, get_object_or_404

from . models import Blog

# Create your views here.

def allblogs(request):
    allblogs = Blog.objects.order_by('-pub_date').all()
    return render(request, 'blog/allblogs.html', {'allblogs': allblogs})


def details(request, blog_id):
    blog_details = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/details.html', {'blog': blog_details})
