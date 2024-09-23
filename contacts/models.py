from django.db import models
from datetime import datetime
# Create your models here.


from django.db import models
from datetime import datetime

class Contact(models.Model):
    listing = models.CharField(max_length=200)
    listing_id = models.IntegerField()
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    phone = models.CharField(max_length=20)  # Changed to CharField to handle various phone formats
    message = models.TextField(blank=True)
    contact_date = models.DateTimeField(default=datetime.now, blank=True)
    user_id = models.IntegerField(blank=True)
    realtor_email = models.EmailField(max_length=200, blank=True)  # Added this line

    def __str__(self) -> str:
        return self.name
