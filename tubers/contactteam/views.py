from django.shortcuts import render
from .models import Contactteam
from django.contrib import messages

# Create your views here.

def contactteam(request):
    if request.method == 'POST':
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        company_name = request.POST['company_name']
        subject = request.POST['subject']
        message = request.POST['message'] 
        user_id = request.POST['user_id']


        #TODO: do all sanitization
 
        contactteam = Contactteam(name=name, phone=phone,email=email, company_name=company_name,subject=subject, message=message, user_id=user_id)
        contactteam.save()
        messages.success(request, 'Thanks for reaching out!')
        return redirect('home')