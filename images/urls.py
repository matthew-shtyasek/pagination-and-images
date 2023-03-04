from django.urls import path

from images.views import images_list_view

app_name = 'images'

urlpatterns = [
    path('', images_list_view, name='imgs'),
]