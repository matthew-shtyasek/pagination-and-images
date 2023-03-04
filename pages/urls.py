from django.urls import path

from pages.views import post_list_view

app_name = 'pages'

urlpatterns = [
    path('posts/', post_list_view, name='posts'),
]