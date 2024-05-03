from django.db import models

from django.contrib.auth.models import AbstractUser

# Create your models here.

#
# username= abhisheksahoo
# password= abhi1573#
class job_seeker_details(models.Model):
    first_name = models.CharField(null=True, blank=True,max_length=40)
    last_name = models.CharField(null=True, blank=True, max_length=40)
    profile_image = models.ImageField(upload_to='static/profile_images/',null=True, blank=True,)
    userid=models.CharField(null=True,blank=True,max_length=40)
    city = models.CharField(null=True, blank=True,max_length=10)
    state = models.CharField(null=True, blank=True,max_length=40)
    Email_id = models.CharField(null=True, blank=True,max_length=40)
    gender=models.CharField(null=True, blank=True,max_length=40)
    date_of_birth = models.CharField(null=True, blank=True,max_length=40)
    # intrested_in = models.CharField(null=True, blank=True,max_length=40)
    education = models.CharField(null=True, blank=True,max_length=40)
    mobile_number = models.CharField(null=True, blank=True,max_length=40)


    def __str__(self):
        return self.first_name or "No Name"



class job_apply_detail(models.Model):
    full_name = models.CharField(null=True, blank=True,max_length=40)
    email_id = models.CharField(null=True, blank=True, max_length=40)
    # profile_image = models.ImageField(upload_to='profile_images/')
    phone_number= models.CharField(null=True, blank=True,max_length=10)
    position = models.CharField(null=True, blank=True,max_length=40)
    salary = models.CharField(null=True, blank=True,max_length=40)
    resume=models.FileField(upload_to='../static/resume/')
    date_of_birth = models.CharField(null=True, blank=True,max_length=40)
    # intrested_in = models.CharField(null=True, blank=True,max_length=40)
    about = models.CharField(null=True, blank=True,max_length=40)
    heighest_qualification = models.CharField(null=True, blank=True,max_length=40)
    skills = models.CharField(null=True, blank=True,max_length=40)


    def __str__(self):
        return self.full_name or "No Name"




# class CustomUser(AbstractUser):
#     email_id2 = models.CharField(max_length=50,unique=True, default='', null=True, blank=True)
#     password = models.CharField(max_length=128)
#
#     def __str__(self):
#         return self.email_id2 or "No Name"
#
#
#

