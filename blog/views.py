from django.shortcuts import render
from django.utils import timezone  #najpierw importy django
from .models import Post           #dopiero potem importy aplikacji

# Create your views here.
# def post_list(request):
#     return render(request, 'blog/post_list.html', {})
#
# #render oznacza ze zostanie przyjety request, poszuka templatki w katalogu post list
#
def archive_post(request):
    return render(request, 'blog/archive_post.html', {})

#dane dynamiczne w szblonach django
def post_list(request):
    # posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    posts = Post.objects.all().order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts':posts})
