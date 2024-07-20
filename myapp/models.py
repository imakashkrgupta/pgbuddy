from django.db import models
import datetime
import os

#Added Manually
from django.contrib.auth.models import User

# Create your models here.
def filepath(request, filename):
    old_filename = filename
    timeNow = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s" % (timeNow, old_filename)
    return os.path.join('uploads/', filename)


#Creating a MODEL for the Post data
class pg_data(models.Model):
    name=models.CharField(max_length=200)
    price=models.IntegerField()
    pgfor=models.CharField(max_length=200, blank=True)
    college=models.CharField(max_length=200)
    distance=models.IntegerField()
    address=models.CharField(max_length=200, blank=True)
    image1=models.ImageField(upload_to=filepath, null=True, blank=True)
    image2=models.ImageField(upload_to=filepath, null=True, blank=True)
    image3=models.ImageField(upload_to=filepath, null=True, blank=True)
    discription=models.CharField(max_length=200)
    email=models.CharField(max_length=100, blank=True)
    phone=models.CharField(max_length=100, blank=True)
    status=models.CharField(max_length=100, default='active')

#Creating a MODEL for the User data
class user_data(models.Model):
    user_name = models.CharField(max_length=200)
    user_email = models.CharField(max_length=200)
    user_phone = models.CharField(max_length=200)
    user_password = models.CharField(max_length=200)