from django.contrib import messages
from django.http.response import HttpResponseRedirect  
from django.shortcuts import redirect, render,HttpResponse
from django.views import View
from django.contrib.auth.models import User 
from .forms import LoginForm ,RegisterForm
from django.contrib.auth import login, authenticate, logout
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required, permission_required
from django.conf import settings

@method_decorator(login_required,name='dispatch')
class Home(View):
    
    def get(self,request):
        return render(request,'html/home.html')
    
class Register(View):
    
    def get(self,request):
        form=RegisterForm()
        ctx={'form':form}
        return render(request,'html/register.html',ctx)
    
    def post(self,request):
        
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            user =User.objects.get(username=username)
            if user:
                messages.success(request, 'Alrwady exixts')
                return redirect('register')
            else:    
                password = form.cleaned_data.get('password')
                confirm_password= form.cleaned_data.get('confirm_password')
                if password == confirm_password:
                    user = User.objects.create(username=username,password=password)
                    messages.success(request, 'Successfully User Created!')
                    return redirect('login')
                else:
                    messages.success(request, 'Password Not match Created!')
                    return redirect('register')
                
        
        else:
            messages.success(request, 'Not Valid data')
            return HttpResponseRedirect('register')
            
            
        
        
class Login(View):
    
    def get(self,request):
        form=LoginForm()
        ctx={'form':form}
        return render(request,'html/login.html',ctx)
    
    def post(self,request):
        
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username = username, password = password)
            if user:
                login(request, user)
                
                messages.success(request, 'Successfully Logged in!')
                return redirect('home')
            else:
                messages.warning(request, 'You are not authenticated')
                return redirect('login')


class Logout(View):
    
    def get(self,request):
        logout(request)

        return HttpResponseRedirect(settings.LOGIN_URL)