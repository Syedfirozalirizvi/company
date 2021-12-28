from django.contrib import messages
from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import LoginForm
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
        form=UserCreationForm()
        ctx={'form':form}
        return render(request,'html/register.html',ctx)
    
    def post(self,request):
        
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully Employee Created!')
            return redirect('login')
        
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