from django.db import models
from django.utils import timezone


class Imggal(models.Model):
    img_title = models.CharField(max_length=100)
    img_description = models.CharField(max_length=500)
    image = models.ImageField(upload_to='images/')
    created_date = models.DateTimeField('date created', default=timezone.now)

    class Meta:
        verbose_name_plural = "Images in gallery"


