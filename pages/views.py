from django.core.paginator import Paginator, EmptyPage
from django.shortcuts import render

from pages.models import Post


def post_list_view(request, page_num=1):
    posts = Post.objects.filter(published=True)

    paginator = Paginator(posts, 2)

    try:
        page_object = paginator.page(page_num)
    except EmptyPage:
        if page_num < 1:
            page_object = paginator.page(1)
        else:
            page_object = paginator.page(paginator.num_pages)

    return render(request, 'pages/post_list.html', {'page': page_object})
