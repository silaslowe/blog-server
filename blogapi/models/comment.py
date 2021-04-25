from django.db import models

class Comment(models.Model):

    comment_body = models.CharField(max_length=300)
    comment_date = models.DateTimeField(auto_now_add=True)
    comment_author = models.CharField(max_length=60)
    comment_approved = models.BooleanField(default=False)