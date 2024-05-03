from django.urls import path, include
from . import views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [

    # path('', views.index_page),
    path('client_js_signup/',views.client_js_signup, name='client_js_signup'),
    path('client_js_signin/',views.client_js_signin, name='client_js_signin'),
    path('client_js_index/',views.client_js_index, name='client_js_index'),
    path('jobdetail/',views.detailjobs, name='jobdetail'),
    path('jobapply/',views.job_apply_entry, name='jobapply'),

    path('<str:form_job_title>/<str:form_job_skills>/', views.job_details, name='job_details'),



]
