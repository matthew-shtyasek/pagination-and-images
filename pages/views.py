from django.core.paginator import Paginator
from django.shortcuts import render

from pages.models import Post


def post_list_view(request, page_num):
    posts = Post.objects.filter(published=True)

    paginator = Paginator(posts, 2)

    page_object = paginator.page(page_num)

    return render(request, 'pages/post_list.html', {'page': page_object})
