from django.db import models

class Subscriber(models.Model):
    name = models.CharField(max_length=40)
    email = models.EmailField()
    subscription_date = models.DateTimeField(auto_now_add=True)
    city = models.CharField(max_length=40)
    state = models.CharField(max_length=2)