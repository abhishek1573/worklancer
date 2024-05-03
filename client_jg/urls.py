from django.urls import path, include
from . import views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [


    # path('', views.index_page),
    path('client_jg_signup/',views.client_jg_signup, name='client_jg_signup'),
    path('client_jg_signin/',views.client_jg_signin, name='client_jg_signin'),
    path('client/', views.client, name="client"),
    path('client_jg_index/', views.client_jg_index, name="client_jg_index"),
    path('job_detail_form/', views.job_detail_form, name="job_detail_form"),
    path('job_apply_detail/', views.apply_detail, name="job_apply_details"),



]
