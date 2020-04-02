from django.db import models

class contactus(models.Model):
    """ contactus apis """
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    subject = models.CharField(max_length=255)
    message = models.CharField(max_length=555)


class subscribe(models.Model):
    """ email subscriber """
    email = models.EmailField(max_length=255)