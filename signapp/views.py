from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from studentapp.models import UserInfo
# Create your views here.


def login_view(request):
    
    userinfo = UserInfo()
    if request.method == 'POST' and 'btn-login' in request.POST:
        login_username = request.POST.get('username').lower()
        login_password = request.POST.get('password')

        if login_password=="" or login_username=="":
            messages.error(request,"Fill Username and Password!")
        else:
            user = authenticate(username = login_username, password = login_password)
            if user :
                if user.is_active:
                    login(request,user)
                    messages.success(request, 'Successfull Login')
                    return redirect('profile_edit')
                else:
                    messages.error(request,"This Id is Blocked!")
            else:
                messages.error(request,"Wrong username or password!")

    return render(request, 'signup/login.html')




def register_view(request):
    if request.method == 'POST' and 'btn-reg' in request.POST:
        reg_username = request.POST.get('username').lower().replace(" ", "")
        reg_password = request.POST.get('password')
        reg_email = request.POST.get('email')

        if reg_email=="" or reg_password =="" or reg_username=="":
            messages.error(request,"Fill Email, Username and Password!")
        elif User.objects.filter(email = reg_email).count() != 0:
            messages.error(request,"email exists! Try another!")
        elif User.objects.filter(username = reg_username).count() != 0:
            messages.error(request,"Username exists! Try another!")

        else:
            user = User.objects.create_user(username=reg_username, password=reg_password,email=reg_email)
            user.save()
            messages.success(request, f'Welcome {user.username}! Please login')
            return redirect('login')
    return render(request, 'signup/register.html')


@login_required
def logout_view(request):
    logout(request)
    messages.success(request, 'Logout Successfull! ')
    return redirect('login')