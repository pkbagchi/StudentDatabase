from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from .models import UserInfo
import os
from PIL import Image
from studentDatabase.settings import MEDIA_DIR
from django.db.models import Q
from django.core.paginator import Paginator
from django.http import Http404

# Create your views here.


@login_required
def profile_edit(request):
    
    hasinfo = True
    click = False
    user = User.objects.get(username=request.user.username)
    try:
        userinfo = UserInfo.objects.get(user = user)
    except:
        hasinfo = False
        userinfo = UserInfo()
        userinfo.user = user
        
    finally:
        if request.method == 'POST' and 'submit_btn' in request.POST:
            userinfo.slug = user.username
            userinfo.user_name = request.POST.get('name').strip()
            userinfo.user_phone =  request.POST.get('phone').strip()
            userinfo.user_bloodGroup =  request.POST.get('blood')
            userinfo.user_gender =  request.POST.get('gender')
            userinfo.user_address =  request.POST.get('address').strip()
            userinfo.user_city =  request.POST.get('city').strip()
            userinfo.user_state =  request.POST.get('state')
            userinfo.user_zip =  request.POST.get('zip').strip()
            userinfo.user_school =  request.POST.get('school').strip()
            userinfo.user_college =  request.POST.get('college').strip()
            userinfo.user_university =  request.POST.get('university').strip()
            userinfo.user_department =  request.POST.get('department').strip()
            userinfo.user_fbId =  request.POST.get('facebook').strip()
            userinfo.user_bio =  request.POST.get('textarea').strip()
            userinfo.bol_field = True
            click = True

            if 'img' in request.FILES :
                
                if  "profile.png" not in str(userinfo.user_picture):
                    img_path =  os.path.join(MEDIA_DIR,userinfo.user_picture.name)
                
                    delete_old_img = True

                userinfo.user_picture = request.FILES.get('img')
        

        hasinfo = True
        
        userinfo.save()
        

        try:
            if delete_old_img:
                os.remove(img_path)
        except:
            pass  
    
    if click:
        messages.success(request, 'Profile Save Successfully!')
        return redirect('home')
       

    return render(request, 'profile_edit.html' ,{'userinfo': userinfo, 'hasinfo':hasinfo})


@login_required
def home(request):

    if request.method == 'POST' and 'btn-search' in request.POST:
        q = request.POST.get('search').strip()
        if q is not None:

            query =  UserInfo.objects.filter(Q(user_name__icontains = q) | Q(user_school__icontains = q) |
                Q(user_college__icontains = q) | Q(user_university__icontains = q) | Q(user_bio__icontains = q)
            ).order_by('-id')
    
            if query.count() == 0:
                messages.error(request, 'No Student Found')
            else :
                pass
    else:
        query = UserInfo.objects.filter(bol_field__iexact = 'True').order_by('-id')
        
    paginator = Paginator(query, 5)  # Show 10 obj per page

    page = request.GET.get('page')
    query = paginator.get_page(page)

    return render(request, 'home.html', {'query' : query})

@login_required
def details_view(request, slug):
    try:
        details_obj = UserInfo.objects.get(slug = slug)
        if slug == str(request.user.username):
            return redirect('profile_edit')
    except:
        if slug == str(request.user.username):
            return redirect('profile_edit')
        else:
            raise Http404("No User Found!")

    return render(request, 'profile_details.html', {'details_obj' : details_obj})
    