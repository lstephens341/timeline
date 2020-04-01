from django.db import models
from taggit.managers import TaggableManager

def path_name(instance, filename):
    return "images2/%s/%s" % (instance.yearField, filename)

class Image(models.Model):
    yearField = models.CharField(max_length=4, default='')
    image = models.FileField(upload_to=path_name)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    caption = models.CharField(max_length=200, default='')
    memories = models.TextField(blank = True)
    tags = models.CharField(max_length=200, default='')


    class Meta:
        ordering = ['yearField']
