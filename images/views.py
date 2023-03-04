from django.shortcuts import render

from images.models import Image


def images_list_view(request):
    image_list = Image.objects.all()
    return render(request, 'images/images.html',
                  context={'images': image_list})
