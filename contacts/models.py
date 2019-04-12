from django.db import models
from datetime import datetime
class Contact(models.Model):
    listing = models.CharField(max_length=200)
    listingId = models.IntegerField()
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    message = models.TextField(blank=True)
    contactDate = models.DateTimeField(default=datetime.now,blank=True)
    userId = models.IntegerField()

    def __str__(self):
        return self.name