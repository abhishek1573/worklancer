from django.db import models

# Create your models here.
from django.db import models

# Create your models here.

class job_giver_details(models.Model):
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


class job_avl_detail(models.Model):
    form_first_name = models.CharField(null=True, blank=True,max_length=40)
    form_last_name = models.CharField(null=True, blank=True, max_length=40)
    jobid= models.CharField(null=True, blank=True, max_length=40)
    job_image = models.ImageField(upload_to='static/images/')
    form_email = models.CharField(null=True, blank=True,max_length=10)
    form_job_title = models.CharField(null=True, blank=True,max_length=40)
    form_phno = models.CharField(null=True, blank=True,max_length=40)
    form_country=models.CharField(null=True, blank=True,max_length=40)
    form_job_desc = models.CharField(null=True, blank=True,max_length=40)
    form_job_skills = models.CharField(null=True, blank=True,max_length=40)



    def __str__(self):
        return self.form_job_title or "No Name"
