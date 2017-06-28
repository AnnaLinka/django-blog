from django.shortcuts import render
from django.utils import timezone  #najpierw importy django
from .models import Post           #dopiero potem importy aplikacji
from django.shortcuts import render, get_object_or_404 #dla błędu
from .forms import PostForm

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

#dla postu o okreslonym numerze, lub gdy nie ma to 404
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

#dla formularza do wpisu postów
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

#do edytowania postów
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})    
