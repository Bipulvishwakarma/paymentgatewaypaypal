from django.shortcuts import render, HttpResponseRedirect
from .models import Product
from django.http import JsonResponse
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
from pathlib import Path
from email.mime.image import MIMEImage
image_path = 'static/images/myimage/my.png'
image_name = Path(image_path).name
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm,Edituserprofile
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout
# Create your views here.

def home(request):
	products = Product.objects.all()
	context = {'products':products}
	return render(request, 'enroll/index.html', context)

def checkout(request, pk,pr):
	product = Product.objects.get(id=pk)
	context = {'product':product}
	#template=render_to_string('enroll/email.html',context)

	email=EmailMessage(
		'Thank you for Donation of $'+str(pr),
		'YOU ARE A HERO',
	settings.EMAIL_HOST_USER,
	[request.user.email],
	)
	email.fail_silently=False
	email.send()
	return render(request, 'enroll/checkout.html', context)

def signup(request):
	if request.method=='POST':
		fm=SignUpForm(request.POST)
		if fm.is_valid():
			fm.save()
	else:
		fm=SignUpForm()


	return render(request,'enroll/signup.html',{'form':fm})


def user_login(request):
	if request.method =='POST':
            fm=AuthenticationForm(request=request,data=request.POST)
            if fm.is_valid():
                uname=fm.cleaned_data['username']
                upass=fm.cleaned_data['password']
                user=authenticate(username=uname,password=upass)
                if user is not None:
                    login(request,user)
                    
                    return HttpResponseRedirect('/home/',{'name':request.user})
	else:
            fm=AuthenticationForm() 				

	return render(request,'enroll/login.html',{'form':fm})

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')


def profile(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            fm=Edituserprofile(request.POST,instance=request.user)
            if fm.is_valid():
                fm.save()
        else:

            fm=Edituserprofile(instance=request.user)
        return render(request,'enroll/profile.html',{'name':request.user,'form':fm})
    else:
        return HttpResponseRedirect('/')

