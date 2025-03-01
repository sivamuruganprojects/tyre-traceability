from django.db import models

class Tyre(models.Model):
    rfid = models.CharField(max_length=100, unique=True)
    status = models.CharField(max_length=50, choices=[("In", "In"), ("Out", "Out")])

    def __str__(self):
        return self.rfid

