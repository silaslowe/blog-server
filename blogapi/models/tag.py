from django.db import models

class Tag(models.Model):
    tag_title = models.CharField(max_length=40)