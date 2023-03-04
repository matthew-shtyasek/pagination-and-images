from django.db import models


class Image(models.Model):
    title = models.CharField(max_length=32)
    create_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='%Y/%m/%d')

    def __str__(self):
        return self.title
