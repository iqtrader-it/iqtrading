from django.db import models
from time import strftime


class Post(models.Model):
    topic = models.CharField(max_length=100, null=False)
    about = models.TextField(max_length=512, null=False)
    content = models.TextField(max_length=4096, null=False)
    image = models.FileField(null=False, upload_to='upload/')
    published = models.DateTimeField(null=False, default=strftime('%Y-%m-%d %H:%M:%S'))
    source = models.URLField(null=True)

    def __str__(self):
        return self.topic
