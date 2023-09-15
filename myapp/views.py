from django.shortcuts import render,redirect

# Create your views here.
from .models import atulmodel

def home(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email= request.POST.get('email')
        subject = request.POST.get('subject')
        msg= request.POST.get('message')
        a = atulmodel.objects.create(
            name = name,
            email = email,
            subject = subject,
            msg = msg
        )
        a.save()  
        return redirect('index')
    return render(request,'index.html')