from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Owner(models.Model):
	ownerName = models.CharField(max_length=20)
	ownerLicense = models.CharField(max_length=50,null=True)
	ownerPicture = models.ImageField(upload_to='img',null=True)
	ownerPassword = models.CharField(max_length=20)
	ownerEmail = models.EmailField(max_length=30)
	ownerPhone = models.CharField(max_length=20)
	remark = models.CharField(max_length=30,null=True)

