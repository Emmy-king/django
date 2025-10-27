from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from django.contrib.auth import authenticate,login,logout
from .models import Profile
from django.contrib import messages

# Create your views here.from django.shortcuts import render

def register(request):
    username = request.POST.get('username')
    email = request.POST.get('email')
    password = request.POST.get('password')
    confirmpassword = request.POST.get('re-pass')

    if not all ([username, email, password, confirmpassword]):
        messages.error(request, "All fields are required")
        return render(request, 'register.html',)
    
    if password != confirmpassword:
        messages.error(request, "Password do not match")
        return render(request, 'register.html',)
    
    if len(username) < 8:
        messages.error(request, "username must be at least 8 characters long")
        return render(request, 'register.html')
    
    if len(password) < 8:
        messages.error(request, "Password must be at least 8 characters long")
        return render(request, 'register.html')
    
    if User.objects.filter(email=email).exists():
        messages.error(request, "Email already exists")
        return render(request, 'register.html ')
    
    if User.objects.filter(username=username).exists():
        messages.error(request, "Username already exists")
        return render(request, 'register.html ')
    
    user = User.objects.create_user (username=username, email=email, password=password)
    user.save()
    messages.success(request, f'{username} created successfully')
    return redirect('login')
    

    return render(request, 'register.html')

def Login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Login successful")
            return redirect('home')
        else:
            messages.error(request, "Invalid username or password")
            return redirect('login')
    return render(request, 'login.html')

def Logout(request):
    logout(request)
    return redirect('home')

def user_profile(request):

    edit = User.objects.get(username=request.user.username)
    profile = Profile.objects.get(user_username=request.user.username)

    if request.method == 'POST':
        profile.image.FILES.get('image') or profile.image
        edit.username = request.POST.get('f-name')
        edit.email = request.POST.get('email')
        profile.save()
        edit.save()
        return redirect('home')
    context = {
        'edited': edit,
        'profiled': profile
    }

    return render(request, 'profile.html')