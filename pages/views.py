from django.shortcuts import render

from pages.models import Post


def post_list_view(request):
    posts = Post.objects.filter(published=True)
    return render(request, 'pages/post_list.html', {'post_list': posts})
