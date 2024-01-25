from django.shortcuts import render, redirect
from django import forms    
#from .models import  user_profile
from .form import *
#from django.contrib.auth.models import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
#from django.contrib import messages
# Create your views here.


def index(request):
    return render(request, 'index.html')

def index1(request):
    return render(request, 'index1.html')


def register(request):
    registered = False
    if request.method == 'POST':
        userForm = user_form(data=request.POST)

        if userForm.is_valid():
            userForm.save()
            registered = True
            return redirect('index1')
            
        else:
            print(userForm.errors)
    
    else:
        userForm = user_form()
        # profileForm = profile_form()
    content = {'userFormed': userForm}
    return render(request, 'register.html', content)

# def user(request):
#     registered = False
#     if request.method == 'POST':
#         profileForm = profile_form(data=request.POST)
#         if profileForm.is_valid:
#             profileForm.save()
#             registered = True

#             if 'profile_pics' in request.FILES:
#                 profileForm.profile_pics = request.FILES['images']
#                 profileForm.save(commit=True)
#                 return redirect('/')

#             else:
#                 print(profileForm.errors)
#                 return redirect('user')
#         else:
#             profileForm = profile_form()
#             return redirect('user')

#     pro_content = {'profile': profileForm}
#     return(request, 'index.html', pro_content)
    
def logout(request):
    logout(request)
    return render(request, 'index.html')
    






# def register(request):
#     pass
# def login(request):
#     pass
# def logout(request):
#     pass
# def index(request):
#     kam = Features.objects.all
#     return render(request, 'index.html', {'features': kam})


# def register(request):
    
#     if request.method == 'POST':
#         username = request.POST['username']
#         email = request.POST['email']
#         password = request.POST['password']
#         repeat_password = request.POST['repeat_password']
        
#         if password == repeat_password:

#             if User.objects.filter(email = email).exists():
#                 messages.info(request, 'This email has already been used')
#                 return redirect('register')
            
#             elif User.objects.filter(username = username).exists():
#                 messages.info(request, 'This username has already been used')
#                 return redirect('register')
#             else:
#                 user = User.objects.create_user(username = username, email = email,
#                                                 password = repeat_password)
#                 user.save()
#                 return redirect('login')
#         else:
#             messages.info(request, 'Password do not match')
#             return redirect('register')
#     else:
#         return render(request, 'register.html')

#     # return render(request, 'login.html')


# def login(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = auth.authenticate(username = username, password = password)
#         if user is not None:
#             auth.login(request, user)
#             return redirect('/')
#         else:
#             messages.info(request, 'pls make sure its correct')
#             return redirect('login')
#     else:
#         return render(request, 'login.html')
    
# def logout(request):
#     auth.logout(request)
#     return redirect('/')



