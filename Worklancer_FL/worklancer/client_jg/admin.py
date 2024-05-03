from django.contrib import admin

# Register your models here.
from . models import *

admin.site.register(job_giver_details)
admin.site.register(job_avl_detail)

