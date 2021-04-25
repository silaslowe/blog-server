from django.db import models

class BlogComment(models.Model):
    blog = models.ForeignKey('Blog', on_delete=models.CASCADE)
    comment = models.ForeignKey('Comment', on_delete=models.CASCADE)