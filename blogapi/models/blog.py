from django.db import models

class Blog(models.Model):
    
    title = models.CharField(max_length=100)
    blog_body = models.CharField(max_length=15000)
    image_url = models.URLField(max_length=100)
    created_on = models.DateTimeField(auto_now_add=True)
