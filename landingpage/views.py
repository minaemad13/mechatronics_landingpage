from django.shortcuts import render
import json
from django.core.mail import send_mail 

from mechatronics_landingpage import settings
# Create your views here.

def index(request):
    if request.method == "GET":
        return render(request,'index.html')
    else:
        try:
            message =f"""
            Dear MechaTronics Team,
                you have an new message from your Website
                
                Sender : {request.POST['name']} / {request.POST['email']}
                
                Message : {request.POST['message']}
                
                Thanks & BR
            """
            send_mail(
                    request.POST['subject'],
                    message,
                    settings.EMAIL_HOST_USER,
                    ['menaemadorai@gmail.com'],
                    fail_silently=False,
                )
            return render(request,'index.html' ,{"success":1})
        except Exception as e:
            return render(request,'index.html' ,{"error":1})
            
           
        