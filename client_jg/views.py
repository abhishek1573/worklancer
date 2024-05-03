from django.shortcuts import render
from . models import *
from client_js.models import *

# Create your views here.
def client_jg_signup(request):

    jg_first_name = request.POST.get('form3Example1m')
    jg_last_name = request.POST.get('form3Example1n')
    jg_profile_photo = request.POST.get('profile_photo')
    jg_userid = request.POST.get('userid')

    jg_city = request.POST.get('form3Example1m1')
    jg_state = request.POST.get('form3Example1n1')
    jg_email_id = request.POST.get('form3Example8')
    jg_gender = request.POST.get('form3Example1ngen')
    jg_dob = request.POST.get('form3Example9')

    jg_edu = request.POST.get('form3Example99')
    jg_phno = request.POST.get('form3Example97')

    user_id_exists = job_giver_details.objects.filter(userid=jg_userid).exists()
    response_data = {'exists': user_id_exists, 'type': 'user_id', 'value': jg_userid}


    if (jg_first_name!=None):
        if user_id_exists:
            return render(request, "client_jg/html/client_jg_signup.html" , {'response_data': response_data})
        else:
            sql = job_giver_details(first_name=jg_first_name, last_name=jg_last_name, profile_image=jg_profile_photo,userid=jg_userid, city=jg_city, state=jg_state,Email_id=jg_email_id, gender=jg_gender, date_of_birth=jg_dob, education=jg_edu,mobile_number=jg_phno)
            sql.save()
            return render(request,"client_jg/html/client_jg_signup.html")
    else:
    
    # print(jg_edu,jg_last_name,jg_first_name)
        return render(request,"client_jg/html/client_jg_signup.html")



def client_jg_signin(request):
    return render(request,"client_jg/html/client_jg_signin.html")



def client(request):
    return render(request, "client_jg/html/client.html")

def job_detail_form(request):

    jform_first_name = request.POST.get('first_name')
    jform_last_name = request.POST.get('last_name')
    jid = request.POST.get('jobid')
    jform_image=request.POST.get('form_img')
    jform_email = request.POST.get('form_email')
    jform_title = request.POST.get('form_jobtitle')
    jform_phno = request.POST.get('jobphno')
    jform_country = request.POST.get('country')
    jform_desc=request.POST.get('descjob')
    jform_skills = request.POST.get('jobskill')
    
    if (jform_title!=None):

        sql = job_avl_detail(form_first_name=jform_first_name, form_last_name=jform_last_name, job_image=jform_image,
                                form_email=jform_email,form_job_title=jform_title, form_phno=jform_phno,
                                form_country= jform_country, form_job_desc= jform_desc,
                                form_job_skills=jform_skills , jobid=jid)
        sql.save()
        return render(request, "client_jg/html/client_jg_job_form.html")
    else:
        return render(request, "client_jg/html/client_jg_job_form.html")


def client_jg_index(request):
    return render (request,"client_jg/html/client_jg_index.html")


def apply_detail(request):
    crse = job_apply_detail.objects.all()
    return render(request,"client_jg/html/job_apply_detail_jg.html",{'crse':crse})