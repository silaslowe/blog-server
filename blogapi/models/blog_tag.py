from django.db import models

class BlogTag(models.Model):
    blog = models.ForeignKey('Blog', on_delete=models.CASCADE)
    tag = models.ForeignKey('Tag', on_delete=models.CASCADE)