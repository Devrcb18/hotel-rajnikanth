from django.db import models

class Seat(models.Model):  # Use capitalized class name
    status = models.CharField(default='empty', max_length=10)
    seatid = models.CharField(max_length=10)
