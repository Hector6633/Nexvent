from django.db import models

# Create your models here.
class Event_Company(models.Model):
    event_img = models.ImageField(upload_to='media')
    event_name = models.CharField(max_length=30)
    event_type = models.CharField(max_length=30)
    event_price = models.BigIntegerField()
    event_description = models.TextField()
    package1 = models.CharField(max_length=30)
    package2 = models.CharField(max_length=30)
    package3 = models.CharField(max_length=30)
    package4 = models.CharField(max_length=30)
    mob_number = models.CharField(max_length=10)
    location = models.CharField(max_length=30)
    
    def __str__(self):
        return self.event_name