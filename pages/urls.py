from django.urls import path

from pages.views import post_list_view

app_name = 'pages'

urlpatterns = [
    path('posts/<int:page_num>/', post_list_view, name='posts'),
    path('posts/', post_list_view, name='first_posts'),
]