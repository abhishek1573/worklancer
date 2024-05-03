from django.shortcuts import render , get_object_or_404

# Create your views here.

from django.shortcuts import render,HttpResponse,redirect
from client_jg.models import *
from . models import job_seeker_details,job_apply_detail
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password

# from django.contrib.auth.models import CustomUser
from django.contrib.auth import authenticate,login,logout



# Create your views here.
def client_js_signup(request):

    password = make_password(request.POST.get('formpassword1'))

    js_first_name = request.POST.get('form3Example1m')
    js_last_name = request.POST.get('form3Example1n')
    js_profile_photo = request.POST.get('profile_photo')
    js_userid = request.POST.get('userid')

    js_city = request.POST.get('form3Example1m1')
    js_state = request.POST.get('form3Example1n1')
    js_gender = request.POST.get('form3Example1ngen')
    js_dob = request.POST.get('form3Example9')
    js_edu = request.POST.get('form3Example99')
    js_phno = request.POST.get('form3Example97')

    js_pass2 = request.POST.get('formpassword2')
    js_email_id = request.POST.get('form3Example8')
    js_pass1 = request.POST.get('formpassword1')

    user_id_exists = job_seeker_details.objects.filter(userid=js_userid).exists()
    response_data = {'exists': user_id_exists, 'type': 'user_id', 'value': js_userid}

    if (js_first_name != None):
        if user_id_exists:
            return render(request, "client_js/html/client_js_signup_page.html" , {'response_data': response_data})
        else:
            print(js_first_name, js_last_name, js_dob)
            sql = job_seeker_details(first_name=js_first_name, last_name=js_last_name, profile_image=js_profile_photo,userid=js_userid,city=js_city, state=js_state,Email_id=js_email_id, gender=js_gender, date_of_birth=js_dob, education=js_edu,mobile_number=js_phno)
            sql.save()
            return render(request, "client_js/html/client_js_signup_page.html")
    else:
        print("not working")
        return render(request, "client_js/html/client_js_signup_page.html")


def client_js_index(request):
    crse = job_avl_detail.objects.all()
    return render(request, "client_js/html/client_js_index.html",{'crse':crse})



def client_js_signin(request):
    return render(request, "client_js/html/client_js_login.html")

# def client_js_signin(request):
#     mailid = request.POST.get('username')
#     password = request.POST.get('password')
#     try:
#         user = CustomUser.objects.get(email_id2=mailid , password=password)
#         print('here',user)
#         print(password)
#         if check_password(password, user.password):
#             # Authentication successful
#             # Store user information in the session for subsequent requests
#             print("hurrrrrrrrrrrrry")
#             return render(request, "client_js/html/client_js_index.html")
#             return redirect('client_js_index')
#
#
#     except CustomUser.DoesNotExist:
#
#
#         return render(request, "client_js/html/client_js_login.html")
#     # return redirect('client_js_index')




def job_details(request, form_job_title,form_job_skills):
    job =job_avl_detail.objects.filter(form_job_title=form_job_title,form_job_skills=form_job_skills)
    return render(request, 'client_js/html/job_apply_form.html', {'job': job})


def job_apply_entry(request):

        japl_name = request.POST.get('name')
        japl_email = request.POST.get('email')
        japl_phno = request.POST.get('phno')
        japl_position= request.POST.get('position')
        japl_sal = request.POST.get('salary')
        japl_resume= request.POST.get('resume')
        japl_aboutyou = request.POST.get('aboutyou')
        japl_heighest_qualif = request.POST.get('heighest_qualif')
        japl_skill= request.POST.get('skill')
        japl_dob= request.POST.get('dob')


        print(japl_phno)
        if (japl_phno!=None):
            sql = job_apply_detail(full_name=japl_name ,email_id =japl_email,
                                     phone_number=japl_phno, position=japl_position,salary=japl_sal,
                                     resume=japl_resume, date_of_birth=japl_dob, about=japl_aboutyou,
                                     heighest_qualification=japl_heighest_qualif, skills=japl_skill)
            sql.save()
            print("done bete")
            crse = job_avl_detail.objects.all()
            return render(request, "client_js/html/client_js_index.html", {'crse': crse})

        else:
            return render(request, "client_js/html/client_js_index.html")






def detailjobs(request):
    crse = job_avl_detail.objects.all()
    return render(request, "client_js/html/jobs_detail.html",{'crse':crse})


# def client_js_signin(request):
#     crse = CustomUser.objects.all()
#     print(crse)
#     mailid = request.POST.get('username')
#     password = request.POST.get('password')
#     CustomUser = authenticate(email_id2=mailid , password=password)
#     print(CustomUser)
#     if CustomUser is not None:
#             login(request, CustomUser)
#             print(CustomUser)
#             return redirect('client_js_index')
#
#     else:
#         return render(request, "client_js/html/client_js_login.html")
#
#


